#include <stdio.h>
#include <math.h>
#include "longsize.h"

/* ********* 
compile with:
gcc -fpic -shared -O2 local_sky_sub.c -o local_sky_sub.so
********* */

INT32 local_sky_sub(int agrc, void *argv[]);
int contains(INT32 *array, INT32 n, INT32 value);

/***********************************************/
/*   this function takes an image from idl     */
/*  and calculates the sky value in an annulus */
/*               near an object                */
/***********************************************/

INT32 local_sky_sub(int agrc, void *argv[]) {
  INT32 i, i2, i3, i4, j, rindex, n, n_loops;
  double dx_sq, dy, r;
  double mean, newmean, oldmean, std, upperlim;

  INT32 minx;
  INT32 maxx;
  INT32 miny;
  INT32 maxy;

  INT32 index;
  INT32 n_pixels;

  /* variables passed from/to IDL */
  float *image;            /* pointer to the image array */
  INT32 n_row;             /* number of rows on the image*/
  INT32 n_col;             /* number of colums on the image*/
  float x;                 /* x coordinate of the object */
  float y;                 /* y coordinate of the object */
  float radius1;           /* inner radius of anulus */
  float radius2;           /* outter radius of anulus */
  INT32 *mask;             /* indicies of all pixles to reject */
  INT32 n_mask;            /* number of pixels to mask */
  float *sky_value;        /* RET: the average sky value in the annulus */
  float *sky_sigma;        /* RET: the standard deviation of the sky in the annulus */
  INT32 *annulus;          /* RET: indicies of all the pixels in the annulus */
  INT32 doreject;          /* boolean for doing rejection */
  INT32 *rejected;         /* RET: indicies of pixels rejected */
  
  /* malloced variables for internal use */
  float *sky_buff;         /* aray holding all the pixel values in the anulus */
  float *tempp;

  /* get the input form IDL */
  index=0;
  image=(float *) argv[index++];
  n_row=*(INT32 *) argv[index++];
  n_col=*(INT32 *) argv[index++];
  x=*(float *) argv[index++];
  y=*(float *) argv[index++];
  radius1=*(float *) argv[index++];
  radius2=*(float *) argv[index++];
  mask=(INT32 *) argv[index++];
  n_mask=*(INT32 *) argv[index++];
  sky_value=(float *) argv[index++];
  sky_sigma=(float *) argv[index++];
  annulus=(INT32 *) argv[index++];
  doreject=*(INT32 *) argv[index++];
  rejected=(INT32 *) argv[index++];

  
  /* allocate memory */
  n_pixels=2*M_PI*pow(radius2+2,2);
  sky_buff=(float *) calloc(n_pixels,sizeof(float));
  if(sky_buff==NULL) {
    printf("local_sky_sub.c: [error 1] cannot allocate required memory...returning\n\r");
    return 0;
  }

  /* find the xy range */
  minx=(x-radius2-1 > 0) ? x-radius2-1 : 0;
  maxx=(x+radius2+1 < n_col) ? x+radius2+1 : n_col;
  miny=(y-radius2-1 > 0) ? y-radius2-1 : 0;
  maxy=(y+radius2+1 < n_row) ? y+radius2+1 : n_row;

  mean=0;
  index=0;
  for(i=minx; i<maxx; i++) {
    dx_sq=pow((x-i),2);
    
    for(j=miny; j<maxy; j++) {
      /* only include points in the annulus that aren't masked */
      if(contains(mask,n_mask,i+n_col*j)) continue;

      dy=(y-j);
      r=sqrt(dx_sq+pow(dy,2));
      
      if(r > radius1 && r < radius2) {
        /* see if we're out of reserved memory; realloc */
        if(index >= n_pixels) {
          n_pixels=(INT32)(1.2*n_pixels);
          tempp=(float *)realloc(sky_buff,sizeof(float)*n_pixels);
          if(tempp==NULL) {
            printf("local_sky_sub.c: [error 2] cannot allocate required memory...returning\n\r");
            free(sky_buff);
            return 0;
          } else {
            sky_buff=tempp;
          }
        }

        /* add the pixel value to the sky buffer */
        sky_buff[index]=image[i+n_col*j];
        annulus[index]=i+n_col*j;
          
        mean+=image[i+n_col*j];
        index++;
      }
    }
  }
  if(index == 0) {
    free(sky_buff);
    return 0;
  }
  if(index == 1) {  /* can't get std from only 1 point */
    free(sky_buff);
    *sky_value=sky_buff[0];
    return 1;
  }
  mean/=index;
  
  /* get the standard deviation */
  std=0;
  for(i=0; i<index; i++) std+=pow(sky_buff[i]-mean,2);
  std/=(index-1);
  std=sqrt(std);


  /* ******************** */
  /* reject object pixels */
  /* ******************** */
  if(n_mask==0) upperlim=3.0;
  else upperlim=4.0;
  j=0;
  n_loops=0;
  while(doreject==1 && n_loops < 10 && (n_loops==0 || fabs(mean-oldmean)/mean > 0.00001)) {
    oldmean=mean;
    
    for(i=0; i<index; i++) {
      if(sky_buff[i]-mean > (upperlim+0.25*n_loops)*std || mean-sky_buff[i] > 5.0*std) {
        
        /* reject this pixel and the 5x5 box arround it */
        for(i2=-2; i2<3; i2++) {
          for(i3=-2; i3<3; i3++) {
            rindex=annulus[i]+i2+i3*n_col;
            
            /* see if this pixel was already rejected */
            if(contains(rejected,j,rindex)) continue;
            
            /* add index to rejected list */
            for(i4=0; i4<index; i4++) {
              if(annulus[i4]==rindex) {
                rejected[j++]=rindex;
                break;
              }
            }
          }
        }
      }
    }
    
    /* find the new mean */
    n=0;
    newmean=0;
    for(i=0; i<index; i++) {
      /* add this pixel to the average if not rejected */
      if(contains(rejected,j,annulus[i])) continue;
      newmean+=sky_buff[i];
      n++;
    }
    mean=newmean/n;
    
    /* find the new standard deviation */
    std=0;
    for(i=0; i<index; i++) {
      if(contains(rejected,j,annulus[i])) continue;
      
      std+=pow(sky_buff[i]-mean,2);
    }
    std/=(n-1);
    std=sqrt(std);
    
    n_loops++;
  }

  if(doreject==0 || n != 0) {
    *sky_sigma=std;
    *sky_value=mean;
  }

  free(sky_buff);
  return n;  
}


/* *************************** */
/* returns 1 if array contains value; otherwise 0; */
int contains(INT32 *array, INT32 n, INT32 value) {
  INT32 i;

  for(i=0; i<n; i++) if(array[i]==value) return 1;

  return 0;
}
