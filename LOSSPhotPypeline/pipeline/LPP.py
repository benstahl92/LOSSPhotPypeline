





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-KYH8zRCvGYQoVsdDKgYaJRXDN9CwQu0YkPVgbKm4cOiqLAxNisg2Kjex6tfrEB3yTAwtXcFY/sxBVj/3IkIiqg==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-a70126cbff30372f13f599b76353080b.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-L+Xfjk72/sIPS5T8Z8Wy/+/78ngrN7jAjVpE5Zoo2KfZYqr9s8p6selV7sLydYrh0Y3Pu02CuEa7uuq70RjSxg==" rel="stylesheet" href="https://github.githubassets.com/assets/site-278e4176d194ae782983c71f1f767503.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-CWBwRMnzx96rZaDFs+PXFA3FHL49ITEoh69OO2lA5vvEAuuh2xA5vyEOPm7PpMhZkAe6xh/Ln3fAsFsbNmmkQg==" rel="stylesheet" href="https://github.githubassets.com/assets/github-44b7ec0f7065626e836351e31ca83577.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>LOSSPhotPypeline/LPP.py at master · benstahl92/LOSSPhotPypeline · GitHub</title>
    <meta name="description" content="Lick Observatory Supernova Search Photometry Pipeline - benstahl92/LOSSPhotPypeline">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/13010209?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="benstahl92/LOSSPhotPypeline" /><meta property="og:url" content="https://github.com/benstahl92/LOSSPhotPypeline" /><meta property="og:description" content="Lick Observatory Supernova Search Photometry Pipeline - benstahl92/LOSSPhotPypeline" />

  <link rel="assets" href="https://github.githubassets.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="B81A:9F78:1DF1F3A:2CAA1EC:5C673BFA" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="B81A:9F78:1DF1F3A:2CAA1EC:5C673BFA" /><meta name="octolytics-dimension-region_edge" content="sea" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MWQ4Y2FjZGJiM2NiOWFkNGM0MWM5ZjZmY2UyNDMyZGQ5MzMxY2U4ZjA5NGI5NDEyZGQxNzhkZjMwYzdjMzExNXx7InJlbW90ZV9hZGRyZXNzIjoiMTM2LjE1Mi4yMjcuMTUxIiwicmVxdWVzdF9pZCI6IkI4MUE6OUY3ODoxREYxRjNBOjJDQUExRUM6NUM2NzNCRkEiLCJ0aW1lc3RhbXAiOjE1NTAyNjk0MzQsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR,MARKETPLACE_BROWSING_V2">

  <meta name="html-safe-nonce" content="2cb41ee6ccb6d5858cf88e09ecbc06ca199a4662">

  <meta http-equiv="x-pjax-version" content="362b0bd9cef47789343c8a97482599e0">
  

      <link href="https://github.com/benstahl92/LOSSPhotPypeline/commits/master.atom" rel="alternate" title="Recent Commits to LOSSPhotPypeline:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/benstahl92/LOSSPhotPypeline git https://github.com/benstahl92/LOSSPhotPypeline.git">

  <meta name="octolytics-dimension-user_id" content="13010209" /><meta name="octolytics-dimension-user_login" content="benstahl92" /><meta name="octolytics-dimension-repository_id" content="147730107" /><meta name="octolytics-dimension-repository_nwo" content="benstahl92/LOSSPhotPypeline" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="147730107" /><meta name="octolytics-dimension-repository_network_root_nwo" content="benstahl92/LOSSPhotPypeline" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/benstahl92/LOSSPhotPypeline/blob/master/LOSSPhotPypeline/pipeline/LPP.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">




  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        
<header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out d-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-none">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0" aria-label="Global">
          <ul class="d-flex list-style-none">
              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0  p-4 left-n4 position-absolute">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features/actions" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions">Actions</a>
                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/case-studies" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Case studies">Case Studies <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class=" mr-3 mr-lg-3">
                <a href="/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, click, go to Enterprise">Enterprise</a>
              </li>

              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0  p-4 left-n4 position-absolute">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                      <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class=" mr-3 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0  p-4 left-n4 position-absolute">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare features">Compare plans</a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare features">Contact Sales</a></li>
                    </ul>

                    <ul class="list-style-none mb-0  border-top pt-3">
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-flex flex-items-center px-0 text-center text-left">
          <div class="d-lg-flex mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="147730107" data-scoped-search-url="/benstahl92/LOSSPhotPypeline/search" data-unscoped-search-url="/search" action="/benstahl92/LOSSPhotPypeline/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=bZxDqj9rTSlKHh4zdjay9WbZtOC37kL/snpvUCJbWoFA29LmR8isRnvM3KIybYGX6EE4IZJDanL5zADedv+48Q=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a class="HeaderMenu-link no-underline mr-3" href="/login?return_to=%2Fbenstahl92%2FLOSSPhotPypeline%2Fblob%2Fmaster%2FLOSSPhotPypeline%2Fpipeline%2FLPP.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign&nbsp;in</a>
          <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign&nbsp;up</a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div role="main" class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      


  





  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Fbenstahl92%2FLOSSPhotPypeline"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/benstahl92/LOSSPhotPypeline/watchers"
     aria-label="1 user is watching this repository">
    1
  </a>

  </li>

  <li>
        <a href="/login?return_to=%2Fbenstahl92%2FLOSSPhotPypeline"
      class="btn btn-sm btn-with-count tooltipped tooltipped-s"
      aria-label="You must be signed in to star a repository" rel="nofollow">
      <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
      Star
    </a>

    <a class="social-count js-social-count" href="/benstahl92/LOSSPhotPypeline/stargazers"
      aria-label="0 users starred this repository">
      0
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fbenstahl92%2FLOSSPhotPypeline"
        class="btn btn-sm btn-with-count tooltipped tooltipped-s"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/benstahl92/LOSSPhotPypeline/network/members" class="social-count"
       aria-label="1 user forked this repository">
      1
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=13010209" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/benstahl92">benstahl92</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/benstahl92/LOSSPhotPypeline">LOSSPhotPypeline</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /benstahl92/LOSSPhotPypeline" href="/benstahl92/LOSSPhotPypeline">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /benstahl92/LOSSPhotPypeline/issues" href="/benstahl92/LOSSPhotPypeline/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /benstahl92/LOSSPhotPypeline/pulls" href="/benstahl92/LOSSPhotPypeline/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /benstahl92/LOSSPhotPypeline/projects" href="/benstahl92/LOSSPhotPypeline/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts security people /benstahl92/LOSSPhotPypeline/pulse" href="/benstahl92/LOSSPhotPypeline/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>


  </div>
<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
    



  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/benstahl92/LOSSPhotPypeline/blob/5a1154fb0792e32accf6ed2174746fdafdabc661/LOSSPhotPypeline/pipeline/LPP.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:827c48187f3a70e77dba8b0598659696 -->

        <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/site/dismiss_signup_prompt" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="OKJcmgEUWC2FMJ8dGGVdCrQvsqaHlNKypbSAur8bQUMkUwxz3nLrEkqKxOg3sitdz/Wchy6WfyLTsxKj8vmVpQ==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 31 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" href="/join?source=prompt-blob-show" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up">Sign up</a>
        </div>
      </div>
    </div>


    <div class="file-navigation">
      
<details class="details-reset details-overlay select-menu branch-select-menu float-left">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
  </summary>

  <details-menu class="select-menu-modal position-absolute" style="z-index: 99;" src="/benstahl92/LOSSPhotPypeline/ref-list/master/LOSSPhotPypeline/pipeline/LPP.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

      <div class="BtnGroup float-right">
        <a href="/benstahl92/LOSSPhotPypeline/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/benstahl92/LOSSPhotPypeline"><span>LOSSPhotPypeline</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/benstahl92/LOSSPhotPypeline/tree/master/LOSSPhotPypeline"><span>LOSSPhotPypeline</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/benstahl92/LOSSPhotPypeline/tree/master/LOSSPhotPypeline/pipeline"><span>pipeline</span></a></span><span class="separator">/</span><strong class="final-path">LPP.py</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/benstahl92/LOSSPhotPypeline/commit/5a1154fb0792e32accf6ed2174746fdafdabc661" data-pjax>
          5a1154f
        </a>
        <relative-time datetime="2019-02-15T19:54:29Z">Feb 15, 2019</relative-time>
      </span>
      <div>
        <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=13010209" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/benstahl92"><img class="avatar" src="https://avatars3.githubusercontent.com/u/13010209?s=40&amp;v=4" width="20" height="20" alt="@benstahl92" /></a>
        <a class="user-mention" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=13010209" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/benstahl92">benstahl92</a>
          <a data-pjax="true" title="improve ref check to include ref stars that are within a specified percentage of images, after iteratively searching" class="message" href="/benstahl92/LOSSPhotPypeline/commit/5a1154fb0792e32accf6ed2174746fdafdabc661">improve ref check to include ref stars that are within a specified pe…</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary
      class="btn-link"
      aria-haspopup="dialog"
      
      
      >
    
    <span><strong>1</strong> contributor</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/benstahl92">
                <img class="avatar mr-2" alt="" src="https://avatars3.githubusercontent.com/u/13010209?s=40&amp;v=4" width="20" height="20" />
                benstahl92
</a>            </li>
        </ul>

  </details-dialog>
</details>
      
    </div>
  </div>





    <div class="file ">
      
<div class="file-header">

  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/benstahl92/LOSSPhotPypeline/raw/master/LOSSPhotPypeline/pipeline/LPP.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/benstahl92/LOSSPhotPypeline/blame/master/LOSSPhotPypeline/pipeline/LPP.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/benstahl92/LOSSPhotPypeline/commits/master/LOSSPhotPypeline/pipeline/LPP.py">History</a>
    </div>



        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      1492 lines (1272 sloc)
      <span class="file-info-divider"></span>
    67.7 KB
  </div>
</div>

      

  <div itemprop="text" class="blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> standard imports</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> glob</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> inspect</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> pprint <span class="pl-k">import</span> pprint</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pickle <span class="pl-k">as</span> pkl</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> copy</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tqdm <span class="pl-k">import</span> tqdm</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> logging</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> subprocess</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> warnings</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> plt</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy.io <span class="pl-k">import</span> fits</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy.wcs <span class="pl-k">import</span> <span class="pl-c1">WCS</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy.coordinates <span class="pl-k">import</span> SkyCoord, match_coordinates_sky</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy.visualization <span class="pl-k">import</span> ZScaleInterval</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy <span class="pl-k">import</span> units <span class="pl-k">as</span> u</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> astropy.utils.exceptions <span class="pl-k">import</span> AstropyWarning</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">warnings.simplefilter(<span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span>, AstropyWarning)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">from</span> p_tqdm <span class="pl-k">import</span> p_map</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    _parallel <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ModuleNotFoundError</span>:</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>package &quot;p_tqdm&quot; not installed, cannot do parallel processing<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    _parallel <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> internal imports</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> LOSSPhotPypeline</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> LOSSPhotPypeline.utils <span class="pl-k">as</span> LPPu</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> LOSSPhotPypeline.image <span class="pl-k">import</span> Phot, FitsInfo, FileNames</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> setup tqdm for pandas</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">tqdm.pandas()</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">LPP</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>Lick Observatory Supernova Search Photometry Reduction Pipeline<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">targetname</span>, <span class="pl-smi">interactive</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-smi">parallel</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-smi">cal_diff_tol</span> <span class="pl-k">=</span> <span class="pl-c1">0.05</span>, <span class="pl-smi">force_color_term</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">                 <span class="pl-smi">wdir</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">override_ref_check</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-smi">sep_tol</span> <span class="pl-k">=</span> <span class="pl-c1">8</span>, <span class="pl-smi">pct_increment</span> <span class="pl-k">=</span> <span class="pl-c1">0.05</span>, <span class="pl-smi">in_pct_floor</span> <span class="pl-k">=</span> <span class="pl-c1">0.8</span>):</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>Instantiation instructions<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> basics from instantiation</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.targetname <span class="pl-k">=</span> targetname.replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.config_file <span class="pl-k">=</span> targetname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.conf<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.interactive <span class="pl-k">=</span> interactive</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wdir <span class="pl-k">=</span> os.path.abspath(wdir) <span class="pl-c"><span class="pl-c">#</span> working directory for running (particularly idl code)</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (parallel <span class="pl-k">is</span> <span class="pl-c1">True</span>) <span class="pl-k">and</span> (_parallel) <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.parallel <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.parallel <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_diff_tol <span class="pl-k">=</span> cal_diff_tol <span class="pl-c"><span class="pl-c">#</span> starting calibration difference tolerance</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.abs_cal_tol <span class="pl-k">=</span> <span class="pl-c1">0.2</span> <span class="pl-c"><span class="pl-c">#</span> do not proceed with the pipeline if in non-interactive mode and cal tol exceeds this</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.min_ref_num <span class="pl-k">=</span> <span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span> minimum number of ref stars</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.pct_increment <span class="pl-k">=</span> pct_increment <span class="pl-c"><span class="pl-c">#</span> amount to increment percentage requirement down by if doing ref check</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.in_pct_floor <span class="pl-k">=</span> in_pct_floor <span class="pl-c"><span class="pl-c">#</span> minimum percentage of images ref stars must be in if doing ref check</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.checks <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>] <span class="pl-c"><span class="pl-c">#</span> default checks to perform on image list</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phase_limits <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">60</span>, <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-c1">365</span>) <span class="pl-c"><span class="pl-c">#</span> phase bounds in days relative to disc. date to keep if &quot;date&quot; check performed</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.override_ref_check <span class="pl-k">=</span> override_ref_check <span class="pl-c"><span class="pl-c">#</span> override requirement that each image have all ref stars</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.sep_tol <span class="pl-k">=</span> sep_tol <span class="pl-c"><span class="pl-c">#</span> radius around target in arcseconds to exclude candidate reference stars from</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> log file</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.logfile <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname.lower().replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.log<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.build_log()</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> sourced from configuration file</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.targetra <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.targetdec <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.photsub <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refname <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>TBD<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.photlistfile <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>TBD<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> discovery date (mjd)</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.disc_date_mjd <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> check if config file exists -- if not then generate template</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(<span class="pl-c1">self</span>.config_file):</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>No configuration file detected, complete template (<span class="pl-c1">{}</span>) before proceeding.<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.config_file <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.template<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">            LPPu.genconf(<span class="pl-v">targetname</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">config_file</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.config_file <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.template<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> general variables</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.filter_set_ref <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.first_obs <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_cols <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>3.5p<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">3</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>5p<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">5</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>7p<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">7</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>9p<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">9</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>1fh<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">11</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>1.5fh<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">13</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>2fh<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">15</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>psf<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">17</span>}</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calmethod <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>psf<span class="pl-pds">&#39;</span></span> <span class="pl-c"><span class="pl-c">#</span> can be set to any key in phot_cols, but recommended is &#39;psf&#39;</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.image_list <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> list of image file names</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> Phot instance for each image</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.aIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of all images in phot_instances</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> subset of aIndex to work on</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.bfIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of images with unsupported filters</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.ucIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of WCS fail images, even though _c</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.bdIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of images with dates outside of phase boundaries</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.pfIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of photometry failures</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.psfIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of photometry (sub) failures</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cfIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of calibration failures</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.csfIndex <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> indices of calibration (sub) failures</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.noIndex <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.nosIndex <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mrIndex <span class="pl-k">=</span> pd.Index([]) <span class="pl-c"><span class="pl-c">#</span> keep track of indices to remove manually</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">False</span> <span class="pl-c"><span class="pl-c">#</span> track run success</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> calibration variables</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>auto<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calfile <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>TBD<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calfile_use <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>TBD<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.force_color_term <span class="pl-k">=</span> force_color_term</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calibration_dir <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>calibration<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.isdir(<span class="pl-c1">self</span>.calibration_dir):</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">            os.makedirs(<span class="pl-c1">self</span>.calibration_dir)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.radecfile <span class="pl-k">=</span> os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-c1">self</span>.targetname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_radec.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.radec <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_arrays <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> keep track of counts of color terms</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.color_terms <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>kait1<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>kait2<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>kait3<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>kait4<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>nickel1<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>nickel2<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&#39;</span>Landolt<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>}</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.color_terms_used <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> load configuration file</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        loaded <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-k">not</span> loaded:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.loadconf()</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                loaded <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">FileNotFoundError</span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                LPPu.genconf(<span class="pl-v">targetname</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">config_file</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.config_file <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.template<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Configuration could not be loaded. Template generated: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.config_file <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.template<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Specify configuration file (*****.conf) or q to quit &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>q<span class="pl-pds">&#39;</span></span> <span class="pl-k">==</span> response.lower():</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.config_file <span class="pl-k">=</span> response</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> lightcurve variables</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.lc_dir <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>lightcurve<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.lc_base <span class="pl-k">=</span> os.path.join(<span class="pl-c1">self</span>.lc_dir, <span class="pl-s"><span class="pl-pds">&#39;</span>lightcurve_<span class="pl-c1">{}</span>_<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.targetname))</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.lc_ext <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>raw<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>_natural_raw.dat<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&#39;</span>bin<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>_natural_bin.dat<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>_natural_group.dat<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&#39;</span>standard<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>_standard.dat<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> galaxy subtraction variables</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.template_images <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.templates_dir <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>templates<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> steps in standard reduction procedure</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.steps <span class="pl-k">=</span> [<span class="pl-c1">self</span>.load_images,</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.check_images,</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.find_ref_stars,</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.match_refcal_stars,</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.do_galaxy_subtraction_all_image,</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.do_photometry_all_image,</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.get_sky_all_image,</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.do_calibration,</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.get_zeromag_all_image,</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.get_limmag_all_image,</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.generate_lc,</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">                      <span class="pl-c1">self</span>.write_summary]</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> save file</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.savefile <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname.lower().replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.sav<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> os.path.exists(<span class="pl-c1">self</span>.savefile):</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">                load <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Load saved state from <span class="pl-c1">{}</span>? ([y]/n) &gt; <span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.savefile))</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">                load <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>n<span class="pl-pds">&#39;</span></span> <span class="pl-c"><span class="pl-c">#</span> run fresh if in non-interactive mode</span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>n<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> load.lower():</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.load()</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> make sure that the selected calmethod is one of the photmethods</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.calmethod <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod:</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>Calibration method must be one of the photometry methods. Exiting.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>          Configuration File Methods</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">loadconf</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        reads config file and sets class attributes accordingly</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the most accurate accounting of system state is stored in the binary savefile</span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> load config file and try to standardize keys</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">        conf <span class="pl-k">=</span> pd.read_csv(<span class="pl-c1">self</span>.config_file, <span class="pl-v">header</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">comment</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">                           <span class="pl-v">index_col</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">squeeze</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>).replace(np.nan, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        conf.index <span class="pl-k">=</span> conf.index.str.lower()</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> read and set values (including the type)</span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.targetra <span class="pl-k">=</span> <span class="pl-c1">float</span>(conf[<span class="pl-s"><span class="pl-pds">&#39;</span>targetra<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.targetdec <span class="pl-k">=</span> <span class="pl-c1">float</span>(conf[<span class="pl-s"><span class="pl-pds">&#39;</span>targetdec<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photsub<span class="pl-pds">&#39;</span></span>].lower() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>yes<span class="pl-pds">&#39;</span></span>: <span class="pl-c"><span class="pl-c">#</span> defaults to False in all other cases</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.photsub <span class="pl-k">=</span> <span class="pl-c1">True</span> </td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>calsource<span class="pl-pds">&#39;</span></span>].lower() <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>psf<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>sdss<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>apass<span class="pl-pds">&#39;</span></span>]: <span class="pl-c"><span class="pl-c">#</span> only set if a known source is specified</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>calsource<span class="pl-pds">&#39;</span></span>].lower() </td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].lower() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.phot_cols.keys())</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].lower():</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].lower().strip() <span class="pl-k">in</span> <span class="pl-c1">self</span>.phot_cols.keys():</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> [conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].lower().strip()]</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> is not a valid photometry method. Available options are:<span class="pl-pds">&#39;</span></span>.format(conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].strip()))</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.phot_col.keys()))</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Enter selection(s) &gt; <span class="pl-pds">&#39;</span></span>).strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">            proposed <span class="pl-k">=</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">set</span>(proposed).issubset(<span class="pl-c1">set</span>(<span class="pl-c1">self</span>.phot_cols.keys())):</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> proposed</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>At least one of <span class="pl-c1">{}</span> is not a valid photometry method. Available options are:<span class="pl-pds">&#39;</span></span>.format(conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photmethod<span class="pl-pds">&#39;</span></span>].strip()))</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.phot_cols.keys()))</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.photmethod <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Enter selection(s) &gt; <span class="pl-pds">&#39;</span></span>).strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refname <span class="pl-k">=</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>refname<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.photlistfile <span class="pl-k">=</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>photlistfile<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>forcecolorterm<span class="pl-pds">&#39;</span></span>].strip() <span class="pl-k">in</span> <span class="pl-c1">self</span>.color_terms.keys():</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.force_color_term <span class="pl-k">=</span> conf[<span class="pl-s"><span class="pl-pds">&#39;</span>forcecolorterm<span class="pl-pds">&#39;</span></span>].strip()</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> loaded<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.config_file))</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>          Logging</span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">build_log</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>starts and sets up log<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log <span class="pl-k">=</span> logging.getLogger(<span class="pl-s"><span class="pl-pds">&#39;</span>LOSSPhotPypeline<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.setLevel(logging.<span class="pl-c1">DEBUG</span>)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> don&#39;t duplicate entries</span></td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.log.hasHandlers():</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.handlers.clear()</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> internal logging</span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        fh <span class="pl-k">=</span> logging.FileHandler(<span class="pl-c1">self</span>.logfile)</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">        fh.setFormatter(logging.Formatter(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%(asctime)s</span> in <span class="pl-c1">%(funcName)s</span> with level <span class="pl-c1">%(levelname)s</span> ::: <span class="pl-c1">%(message)s</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.addHandler(fh)</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if in interactive mode, print log at or above INFO on screen</span></td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">             sh <span class="pl-k">=</span> logging.StreamHandler()</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">             sh.setLevel(logging.<span class="pl-c1">INFO</span>)</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">             sh.setFormatter(logging.Formatter(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-c1">%(message)s</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span>))</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">             <span class="pl-c1">self</span>.log.addHandler(sh)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> used by contextlib to log all idl and bash outputs, while hiding from screen</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.write <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">msg</span>: <span class="pl-c1">self</span>.log.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>[external] <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> msg) <span class="pl-k">if</span> msg <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>Welcome to the LOSS Photometry Pypeline (LPP)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>          UI / Automation Methods</span></td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__iter__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">next</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>performs next reduction step (arguments for that step can be passed through)<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.current_step <span class="pl-k">&lt;</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.steps):</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step](<span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.save()</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">StopIteration</span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">skip</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>skip current step<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>skipping step: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step].<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.go_to(<span class="pl-c1">self</span>.current_step <span class="pl-k">+</span> <span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">go_to</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">step</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>go to specified step, or choose interactively<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(step) <span class="pl-k">==</span> <span class="pl-c1">int</span>:</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> step</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Choose an option:<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>primary reduction steps:<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i, step <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.steps):</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> i <span class="pl-k">==</span> <span class="pl-c1">self</span>.current_step:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> --- <span class="pl-c1">{}</span> (current step)<span class="pl-pds">&#39;</span></span>.format(i, step.<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> --- <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(i, step.<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>additional options:<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>n  --- add new image(s) by filename(s)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>nf --- add new images from file of names<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>p  --- plot light curve from file<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>c  --- cut points from specific light curve<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>cr --- cut points from specific raw light curve and regenerate subsequent light curves<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>q  --- quit<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">            resp <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>selection &gt; <span class="pl-pds">&#39;</span></span>).lower()</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>n<span class="pl-pds">&#39;</span></span> <span class="pl-k">==</span> resp:</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">                new_images <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>enter name(s) or new images (comma separated) &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> new_images:</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                    new_image_list <span class="pl-k">=</span> [new_images]</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">                    new_image_list <span class="pl-k">=</span> [fl.strip() <span class="pl-k">for</span> fl <span class="pl-k">in</span> new_images.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.process_new_images(<span class="pl-v">new_image_list</span> <span class="pl-k">=</span> new_image_list)</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>nf<span class="pl-pds">&#39;</span></span> <span class="pl-k">==</span> resp:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                new_image_file <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>enter name of new image file &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.process_new_images(<span class="pl-v">new_image_file</span> <span class="pl-k">=</span> new_image_file)</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>p<span class="pl-pds">&#39;</span></span> <span class="pl-k">==</span> resp:</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                lc_file <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>enter light curve file (including relative path) to plot &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_lc([lc_file])</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> (resp <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>c<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> (resp <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cr<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">                lc_file <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>enter light curve file (including relative path) to cut points from &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">                regenerate <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> resp <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cr<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                    regenerate <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.cut_lc_points(lc_file, <span class="pl-v">regenerate</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">int</span>(resp)</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">save</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>saves current state of pipeline<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">        vs <span class="pl-k">=</span> <span class="pl-c1">vars</span>(<span class="pl-c1">self</span>).copy()</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">        vs.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>steps<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">        vs.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>log<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.savefile, <span class="pl-s"><span class="pl-pds">&#39;</span>wb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">            pkl.dump(vs, f)</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> written<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.savefile))</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">load</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">savefile</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>re-initializes pipeline from saved state in file<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> savefile <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">            savefile <span class="pl-k">=</span> <span class="pl-c1">self</span>.savefile</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(savefile, <span class="pl-s"><span class="pl-pds">&#39;</span>rb<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">            vs <span class="pl-k">=</span> pkl.load(f)</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> v <span class="pl-k">in</span> vs.keys():</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">            s <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>self.<span class="pl-c1">{}</span> = vs[&quot;<span class="pl-c1">{}</span>&quot;]<span class="pl-pds">&#39;</span></span>.format(v, v)</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">exec</span>(s)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> loaded<span class="pl-pds">&#39;</span></span>.format(savefile))</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.summary()</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">summary</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>print summary of pipeline status<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span>)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Reduction status for <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.targetname))</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Interactive: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.interactive))</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Photsub Mode: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.photsub))</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.current_step <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Beginning of reduction pipeline.<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Previous step: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step <span class="pl-k">-</span> <span class="pl-c1">1</span>].<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step <span class="pl-k">-</span> <span class="pl-c1">1</span>].<span class="pl-c1">__doc__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>--&gt; Next step: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step].<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step].<span class="pl-c1">__doc__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IndexError</span>:</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>End of reduction pipeline.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.save()</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>----&gt; Subsequent step: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step <span class="pl-k">+</span> <span class="pl-c1">1</span>].<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-c1">self</span>.steps[<span class="pl-c1">self</span>.current_step <span class="pl-k">+</span> <span class="pl-c1">1</span>].<span class="pl-c1">__doc__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IndexError</span>:</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>End of reduction pipeline.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">skips</span> <span class="pl-k">=</span> []):</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>run through reduction steps<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.current_step <span class="pl-k">in</span> skips:</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.skip()</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.next()</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">StopIteration</span>:</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">show_variables</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>prints instance variables<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">        pprint(<span class="pl-c1">vars</span>(<span class="pl-c1">self</span>))</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">show_methods</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>show available methods<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>method: docstring<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> name <span class="pl-k">in</span> <span class="pl-c1">LPP</span>.<span class="pl-c1">__dict__</span>.keys():</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> name[:<span class="pl-c1">2</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> name <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>show_methods<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(name, <span class="pl-c1">LPP</span>.<span class="pl-c1">__dict__</span>[name].<span class="pl-c1">__doc__</span>))</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>          Reduction Pipeline Methods</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">load_images</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>reads image list file to generate lists of image names and Phot instances<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.image_list <span class="pl-k">=</span> pd.read_csv(<span class="pl-c1">self</span>.photlistfile, <span class="pl-v">header</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">                                      <span class="pl-v">comment</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>, <span class="pl-v">squeeze</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Selected image files<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-c1">self</span>.image_list)</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>image list loaded from <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.photlistfile))</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>generating list of Phot instances from image list<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances <span class="pl-k">=</span> <span class="pl-c1">self</span>._im2inst(<span class="pl-c1">self</span>.image_list) <span class="pl-c"><span class="pl-c">#</span> radec is None if running in order</span></td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set indices</span></td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.aIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.image_list.index</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.aIndex</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_images</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>only keep images that are in a supported filter and without file format issues<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> filter check</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.checks:</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">            filter_check <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">img</span>: <span class="pl-c1">True</span> <span class="pl-k">if</span> img.filter.upper() <span class="pl-k">in</span> <span class="pl-c1">self</span>.filter_set_ref <span class="pl-k">else</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>checking filters<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">            bool_idx <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(filter_check)</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.bfIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex[<span class="pl-k">~</span>pd.Series(bool_idx)]</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>dropping <span class="pl-c1">{}</span> images due to unsupported filter<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.bfIndex)))</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.bfIndex)</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> uncal check</span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>uncal<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.checks:</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">            cal_check <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">img</span>: <span class="pl-c1">True</span> <span class="pl-k">if</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>RADECSYS<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> img.header) <span class="pl-k">else</span> (<span class="pl-c1">False</span> <span class="pl-k">if</span> (img.header[<span class="pl-s"><span class="pl-pds">&#39;</span>RADECSYS<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-999<span class="pl-pds">&#39;</span></span>) <span class="pl-k">else</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>checking images for WCS<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">            bool_idx <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(cal_check)</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.ucIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex[<span class="pl-k">~</span>pd.Series(bool_idx)]</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>dropping <span class="pl-c1">{}</span> images for failed WCS<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.ucIndex)))</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.ucIndex)</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.checks:</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.disc_date_mjd <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>discovery date not set, cannot do date check<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">            date_check <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">img</span>: <span class="pl-c1">True</span> <span class="pl-k">if</span> ((img.mjd <span class="pl-k">&gt;=</span> (<span class="pl-c1">self</span>.disc_date_mjd <span class="pl-k">+</span> <span class="pl-c1">self</span>.phase_limits[<span class="pl-c1">0</span>])) <span class="pl-k">and</span> </td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">                         (img.mjd <span class="pl-k">&lt;=</span> (<span class="pl-c1">self</span>.disc_date_mjd <span class="pl-k">+</span> <span class="pl-c1">self</span>.phase_limits[<span class="pl-c1">1</span>]))) <span class="pl-k">else</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>checking phases<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">            bool_idx <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(date_check)</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.bdIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex[<span class="pl-k">~</span>pd.Series(bool_idx)]</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>dropping <span class="pl-c1">{}</span> images that are outside of phase bounds<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.bdIndex)))</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.bdIndex)</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if there are none left, end pipeline</span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>all images removed by checks --- cannot proceed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.write_summary) <span class="pl-k">-</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">find_ref_stars</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>identify all suitable stars in ref image, compute ra &amp; dec, write radecfile, store in instance<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if radecfile already exists, no need to do it</span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> os.path.exists(<span class="pl-c1">self</span>.radecfile):</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>radecfile already exists, loading only<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.radec <span class="pl-k">=</span> pd.read_csv(<span class="pl-c1">self</span>.radecfile, <span class="pl-v">delim_whitespace</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">skiprows</span> <span class="pl-k">=</span> (<span class="pl-c1">0</span>,<span class="pl-c1">1</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>,<span class="pl-c1">5</span>), <span class="pl-v">names</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> set radec in Phot instances</span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> img <span class="pl-k">in</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex]:</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">                img.radec <span class="pl-k">=</span> <span class="pl-c1">self</span>.radec</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.refname <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> :</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>refname has not been assigned, please do it first!<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> instantiate object to manage names</span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">        ref <span class="pl-k">=</span> Phot(<span class="pl-c1">self</span>.refname)</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> use sextractor to extract all stars to be used as refstars</span></td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">        sxcp <span class="pl-k">=</span> os.path.join(os.path.dirname(inspect.getfile(LOSSPhotPypeline)), <span class="pl-s"><span class="pl-pds">&#39;</span>conf<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>sextractor_config<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">        config <span class="pl-k">=</span> os.path.join(sxcp, <span class="pl-s"><span class="pl-pds">&#39;</span>kait.sex<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">        filt <span class="pl-k">=</span> os.path.join(sxcp, <span class="pl-s"><span class="pl-pds">&#39;</span>gauss_2.0_5x5.conv<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">        par <span class="pl-k">=</span> os.path.join(sxcp, <span class="pl-s"><span class="pl-pds">&#39;</span>kait.par<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">        star <span class="pl-k">=</span> os.path.join(sxcp, <span class="pl-s"><span class="pl-pds">&#39;</span>default.nnw<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">        cmd_list <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>sex<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.refname,</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-c<span class="pl-pds">&#39;</span></span>, config,</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-PARAMETERS_NAME<span class="pl-pds">&#39;</span></span>, par,</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-FILTER_NAME<span class="pl-pds">&#39;</span></span>, filt,</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-STARNNW_NAME<span class="pl-pds">&#39;</span></span>, star,</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-CATALOG_NAME<span class="pl-pds">&#39;</span></span>, ref.sobj,</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>-CHECKIMAGE_NAME<span class="pl-pds">&#39;</span></span>, ref.skyfit]</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">        p <span class="pl-k">=</span> subprocess.Popen(cmd_list, <span class="pl-v">stdout</span> <span class="pl-k">=</span> subprocess.<span class="pl-c1">PIPE</span>, <span class="pl-v">stderr</span> <span class="pl-k">=</span> subprocess.<span class="pl-c1">PIPE</span>, <span class="pl-v">universal_newlines</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">        stdout, stderr <span class="pl-k">=</span> p.communicate()</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.debug(stdout)</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.debug(stderr)</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> make sure process succeeded</span></td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(ref.sobj):</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>SExtractor failed --- no sobj file generated, check!<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> read sobj file of X_IMAGE and Y_IMAGE columns, as well as MAG_APER for sort</span></td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> fits.open(ref.sobj) <span class="pl-k">as</span> hdul:</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">            data <span class="pl-k">=</span> hdul[<span class="pl-c1">1</span>].data</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> sort according to magnitude, from small/bright to hight/faint</span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">        data.sort(<span class="pl-v">order</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>MAG_APER<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">        imagex <span class="pl-k">=</span> data.<span class="pl-c1">X_IMAGE</span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">        imagey <span class="pl-k">=</span> data.<span class="pl-c1">Y_IMAGE</span></td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> transform to RA and DEC using ref image header information</span></td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">        cs <span class="pl-k">=</span> WCS(<span class="pl-v">header</span> <span class="pl-k">=</span> ref.header)</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">        imagera, imagedec <span class="pl-k">=</span> cs.all_pix2world(imagex, imagey, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> remove any identified &quot;stars&quot; that are too close to target</span></td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">        coords <span class="pl-k">=</span> SkyCoord(imagera, imagedec, <span class="pl-v">unit</span> <span class="pl-k">=</span> (u.deg, u.deg))</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">        target_coords <span class="pl-k">=</span> SkyCoord(<span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, <span class="pl-v">unit</span> <span class="pl-k">=</span> (u.deg, u.deg))</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">        offsets <span class="pl-k">=</span> coords.separation(target_coords).arcsecond</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">        imagera <span class="pl-k">=</span> imagera[offsets <span class="pl-k">&gt;</span> <span class="pl-c1">self</span>.sep_tol]</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">        imagedec <span class="pl-k">=</span> imagedec[offsets <span class="pl-k">&gt;</span> <span class="pl-c1">self</span>.sep_tol]</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> write radec file</span></td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.radecfile, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>TARGET<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>          RA          DEC<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>   <span class="pl-c1">{<span class="pl-k">:.7f</span>}</span>  <span class="pl-c1">{<span class="pl-k">:.7f</span>}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec))</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>REFSTARS<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>          RA          DEC<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(imagera)):</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">                f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>   <span class="pl-c1">{<span class="pl-k">:.7f</span>}</span>  <span class="pl-c1">{<span class="pl-k">:.7f</span>}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(imagera[i], imagedec[i]))</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> written<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.radecfile))</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.radec <span class="pl-k">=</span> pd.read_csv(<span class="pl-c1">self</span>.radecfile, <span class="pl-v">delim_whitespace</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">skiprows</span> <span class="pl-k">=</span> (<span class="pl-c1">0</span>,<span class="pl-c1">1</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>,<span class="pl-c1">5</span>), <span class="pl-v">names</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set radec in Phot instances</span></td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> img <span class="pl-k">in</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex]:</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">            img.radec <span class="pl-k">=</span> <span class="pl-c1">self</span>.radec</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">match_refcal_stars</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>get calibration catalog, and match stars to ref stars -- only do if needed<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> os.path.exists(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-c1">self</span>.calfile)) <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> get calibration catalog</span></td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">            catalog <span class="pl-k">=</span> LPPu.astroCatalog(<span class="pl-c1">self</span>.targetname, <span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, <span class="pl-v">relative_path</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.calibration_dir)</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">            catalog.get_cal(<span class="pl-v">method</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_source)</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.calfile <span class="pl-k">=</span> catalog.cal_filename</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> catalog.cal_source</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>calibration data sourced<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>matching ref stars to catalog stars and selecting 40 brightest<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.get_cal_info()</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        radec <span class="pl-k">=</span> SkyCoord(<span class="pl-c1">self</span>.radec.loc[<span class="pl-c1">1</span>:, <span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">self</span>.radec.loc[<span class="pl-c1">1</span>:, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>], <span class="pl-v">unit</span> <span class="pl-k">=</span> (u.deg, u.deg))</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">        cal_cat <span class="pl-k">=</span> pd.read_csv(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-c1">self</span>.calfile), <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">        cal <span class="pl-k">=</span> SkyCoord(cal_cat.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>ra<span class="pl-pds">&#39;</span></span>], cal_cat.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>dec<span class="pl-pds">&#39;</span></span>], <span class="pl-v">unit</span> <span class="pl-k">=</span> (u.deg, u.deg))</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">        idx, d2d, d3d <span class="pl-k">=</span> match_coordinates_sky(cal, radec)</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        cal_use <span class="pl-k">=</span> cal_cat.iloc[d2d.arcsecond <span class="pl-k">&lt;</span> <span class="pl-c1">5</span>] <span class="pl-c"><span class="pl-c">#</span> calibration stars that match within 5&quot;</span></td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">        cal_use.index <span class="pl-k">=</span> <span class="pl-c1">self</span>.radec.loc[<span class="pl-c1">1</span>:].iloc[idx[d2d.arcsecond <span class="pl-k">&lt;</span> <span class="pl-c1">5</span>]].index <span class="pl-k">-</span> <span class="pl-c1">1</span> <span class="pl-c"><span class="pl-c">#</span> don&#39;t count sn and align indices with radecfile</span></td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">        cal_use.insert(<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>starID<span class="pl-pds">&#39;</span></span>, cal_use.index)</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">        cal_use <span class="pl-k">=</span> cal_use.sort_values(<span class="pl-v">by</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>).drop_duplicates(<span class="pl-v">subset</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>starID<span class="pl-pds">&#39;</span></span>, <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>first<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_use <span class="pl-k">=</span> cal_use.iloc[:<span class="pl-c1">40</span>] <span class="pl-c"><span class="pl-c">#</span> select top 40 brightest</span></td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> write &quot;use&quot; files</span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-c1">self</span>.calfile_use), <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">            outfile.write(<span class="pl-c1">self</span>.cal_use.to_string(<span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>))</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">        catalog <span class="pl-k">=</span> LPPu.astroCatalog(<span class="pl-c1">self</span>.targetname, <span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, <span class="pl-v">relative_path</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.calibration_dir)</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">        catalog.cal_filename <span class="pl-k">=</span> <span class="pl-c1">self</span>.calfile_use</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">        catalog.cal_source <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_source</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">        catalog.to_natural()</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cal_arrays <span class="pl-k">=</span> catalog.get_cal_arrays(<span class="pl-v">index_order</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_use.index)</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> show ref stars (and cut if interactive mode)</span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._display_refstars(<span class="pl-v">icut</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._display_refstars()</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">do_galaxy_subtraction_all_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>performs galaxy subtraction on all selected image files<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.photsub:</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>not in photsub mode, skipping galaxy subtraction<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>starting galaxy subtraction<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.template_images <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.load_templates()</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.template_images <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>could not get suitable template images, running without galaxy subtraction<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.photsub <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set up for parallelization</span></td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">        ti <span class="pl-k">=</span> <span class="pl-c1">self</span>.template_images</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">        fn <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.galaxy_subtract(ti)</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> do galaxy subtraction in the appropriate mode</span></td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.parallel <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">            res <span class="pl-k">=</span> p_map(fn, <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].tolist())</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">            res <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> img <span class="pl-k">in</span> tqdm(<span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].tolist()):</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">                res.append(fn(img))</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> extract results, log, and determine if successful</span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        res <span class="pl-k">=</span> pd.DataFrame(res, <span class="pl-v">columns</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>success<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>log<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        res[<span class="pl-s"><span class="pl-pds">&#39;</span>log<span class="pl-pds">&#39;</span></span>].apply(<span class="pl-k">lambda</span> <span class="pl-smi">log_entry</span>: <span class="pl-c1">self</span>._log_idl(<span class="pl-k">*</span>log_entry))</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> res[<span class="pl-s"><span class="pl-pds">&#39;</span>success<span class="pl-pds">&#39;</span></span>].all():</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>photsub failed (probably b/c of missing templates), running without galaxy subtraction<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._get_template_candidates()</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.photsub <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>galaxy subtraction done<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">do_photometry_all_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>performs photometry on all selected image files<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>starting photometry (galsub: <span class="pl-c1">{}</span>)<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.photsub))</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set up for parallelization</span></td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">        ps <span class="pl-k">=</span> <span class="pl-c1">self</span>.photsub</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">        fn <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.do_photometry(<span class="pl-v">photsub</span> <span class="pl-k">=</span> ps)</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> do photometry in the appropriate mode</span></td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.parallel <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">            res <span class="pl-k">=</span> p_map(fn, <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].tolist())</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">            res <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> img <span class="pl-k">in</span> tqdm(<span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].tolist()):</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">                res.append(fn(img))</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> extract results, log, and remove failures</span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">        res <span class="pl-k">=</span> pd.DataFrame(res, <span class="pl-v">columns</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>unsub<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>sub<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>log<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">        res[<span class="pl-s"><span class="pl-pds">&#39;</span>log<span class="pl-pds">&#39;</span></span>].apply(<span class="pl-k">lambda</span> <span class="pl-smi">log_entry</span>: <span class="pl-c1">self</span>._log_idl(<span class="pl-k">*</span>log_entry))</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.pfIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex[<span class="pl-k">~</span>res[<span class="pl-s"><span class="pl-pds">&#39;</span>unsub<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>photometry failed on <span class="pl-c1">{}</span> out of <span class="pl-c1">{}</span> images<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.pfIndex), <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)))</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.pfIndex)</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.psfIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex[<span class="pl-k">~</span>res[<span class="pl-s"><span class="pl-pds">&#39;</span>sub<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>photometry (sub) failed on <span class="pl-c1">{}</span> out of <span class="pl-c1">{}</span> images<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.psfIndex), <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)))</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.pfIndex.intersection(<span class="pl-c1">self</span>.psfIndex))</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>all images failed, cannot proceed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.write_summary) <span class="pl-k">-</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>photometry done<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_sky_all_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>get and set sky value for every phot instance<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>getting sky value for each image<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.get_sky())</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">calibrate</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">final_pass</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>performs calibration on all images included in photlistfile, using outputs from do_photometry_all_image<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> final_pass:</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>performing calibration<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>doing final calibration<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> reset trackers</span></td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.color_terms <span class="pl-k">=</span> {key: <span class="pl-c1">0</span> <span class="pl-k">for</span> key <span class="pl-k">in</span> <span class="pl-c1">self</span>.color_terms.keys()}</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.cfIndex <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.csfIndex <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> calibration list</span></td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">        cal_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[<span class="pl-s"><span class="pl-pds">&#39;</span>kait4<span class="pl-pds">&#39;</span></span>].index <span class="pl-c"><span class="pl-c">#</span> choice of color term here is arbitrary</span></td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> iterate through image list and execute calibration script on each</span></td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> idx, img <span class="pl-k">in</span> tqdm(<span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].iteritems(), <span class="pl-v">total</span> <span class="pl-k">=</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)):</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> count usage of color terms</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.force_color_term <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.color_terms[img.color_term] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.color_terms[<span class="pl-c1">self</span>.force_color_term] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> set photsub mode appropriately</span></td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">                ps <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> (<span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">True</span>) <span class="pl-k">and</span> (idx <span class="pl-k">in</span> <span class="pl-c1">self</span>.psfIndex):</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">                ps <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">                ps <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> do calibration</span></td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">            phot <span class="pl-k">=</span> img.calibrate(<span class="pl-c1">self</span>.cal_IDs, <span class="pl-c1">self</span>.cal_arrays[img.color_term].loc[:, img.filter.upper()], <span class="pl-v">sub</span> <span class="pl-k">=</span> ps, <span class="pl-v">write_dat</span> <span class="pl-k">=</span> final_pass)</td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">            phot.rename(<span class="pl-v">columns</span> <span class="pl-k">=</span> {<span class="pl-c1">self</span>.calmethod: <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>}, <span class="pl-v">inplace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> add comparison information</span></td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">            phot.insert(<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Filter<span class="pl-pds">&#39;</span></span>, img.filter.upper())</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">            phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_cal<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[img.color_term].loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">            phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_cal<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[img.color_term].loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">            phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_cal<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[img.color_term].loc[<span class="pl-c1">self</span>.cal_IDs, img.filter.upper()]</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">            phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_diff<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> np.abs(phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_obs<span class="pl-pds">&#39;</span></span>] <span class="pl-k">-</span> phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_cal<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">            phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_diff<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> np.abs(phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_obs<span class="pl-pds">&#39;</span></span>] <span class="pl-k">-</span> phot.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_cal<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">            cal_list.append(phot.loc[<span class="pl-c1">self</span>.cal_IDs, [<span class="pl-s"><span class="pl-pds">&#39;</span>Filter<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_diff<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_diff<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_cal<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ref_in<span class="pl-pds">&#39;</span></span>]])</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> check for success if in final pass mode</span></td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> final_pass:</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (os.path.exists(img.psfdat) <span class="pl-k">is</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.cfIndex.append(idx)</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (<span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">True</span>) <span class="pl-k">and</span> (os.path.exists(img.psfsubdat) <span class="pl-k">is</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.csfIndex.append(idx)</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calibrators <span class="pl-k">=</span> pd.concat([df.loc[<span class="pl-c1">self</span>.cal_IDs, :] <span class="pl-k">for</span> df <span class="pl-k">in</span> cal_list], <span class="pl-v">keys</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex)</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> remove failures if in final pass mode</span></td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> final_pass:</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cfIndex <span class="pl-k">=</span> pd.Series(<span class="pl-c1">self</span>.cfIndex)</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.csfIndex <span class="pl-k">=</span> pd.Series(<span class="pl-c1">self</span>.csfIndex)</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>calibration failed on <span class="pl-c1">{}</span> out of <span class="pl-c1">{}</span> images<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.cfIndex), <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)))</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">self</span>.cfIndex) <span class="pl-c"><span class="pl-c">#</span> processing based only on non-subtracted images</span></td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>calibration (sub) failed on <span class="pl-c1">{}</span> out of <span class="pl-c1">{}</span> images<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.csfIndex), <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)))</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>all images failed, cannot proceed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.write_summary) <span class="pl-k">-</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">do_calibration</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">force_clear</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">use_filts</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>check calibration and make cuts as needed<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>performing calibration<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> get filters used</span></td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.filters <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.filter.upper()))</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> use_filts <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">            use_filts <span class="pl-k">=</span> <span class="pl-c1">self</span>.filters</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> identify ref stars to disregard (if they are not in a sufficient pct of images)</span></td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.override_ref_check <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>finding common ref stars<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> define checking function</span></td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">def</span> <span class="pl-en">check</span>(<span class="pl-smi">img</span>, <span class="pl-smi">imagera</span>, <span class="pl-smi">imagedec</span>):</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">                cs <span class="pl-k">=</span> WCS(<span class="pl-v">header</span> <span class="pl-k">=</span> img.header)</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> ref star location as a fraction of total pixels</span></td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">                r <span class="pl-k">=</span> cs.all_world2pix(np.column_stack([imagera, imagedec]), <span class="pl-c1">0</span>) <span class="pl-k">/</span> np.array(cs._naxis)</td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> good ref stars are within image</span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">                good_ref <span class="pl-k">=</span> np.any(((r <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>) <span class="pl-k">&amp;</span> (r <span class="pl-k">&lt;</span> <span class="pl-c1">1</span>)), <span class="pl-v">axis</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">1</span> <span class="pl-k">*</span> good_ref <span class="pl-c"><span class="pl-c">#</span> express boolean array as 0&#39;s and 1&#39;s</span></td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> color term is arbitrary in next two lines b/c just getting coordinates</span></td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">            imagera <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[<span class="pl-s"><span class="pl-pds">&#39;</span>kait4<span class="pl-pds">&#39;</span></span>].loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">            imagedec <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_arrays[<span class="pl-s"><span class="pl-pds">&#39;</span>kait4<span class="pl-pds">&#39;</span></span>].loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> set iteration params</span></td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">            cal_IDs_tmp <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">            accept <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">            cnt <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-k">not</span> accept:</td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> do the check, and get results as a percentage of images each ref star is in</span></td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">                ref_in_pct <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: check(img, imagera, imagedec)).mean()</td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> determine what to do</span></td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">                current_pct <span class="pl-k">=</span> <span class="pl-c1">1</span> <span class="pl-k">-</span> <span class="pl-c1">self</span>.pct_increment <span class="pl-k">*</span> cnt</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> current_pct <span class="pl-k">&gt;=</span> <span class="pl-c1">self</span>.in_pct_floor:</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">                    cal_IDs_tmp <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs[ref_in_pct <span class="pl-k">&gt;=</span> current_pct]</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>reached minimum tolerance for pct image including ref stars, quitting<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">len</span>(cal_IDs_tmp) <span class="pl-k">&gt;=</span> <span class="pl-c1">self</span>.min_ref_num:</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> ref stars are in at least <span class="pl-c1">{}</span> pct of images, using these<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">len</span>(cal_IDs_tmp), <span class="pl-c1">100</span><span class="pl-k">*</span>current_pct))</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">                    accept <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">                cnt <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> cal_IDs_tmp</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> iterate until acceptable tolerance is reached</span></td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">        accept_tol <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">        skip_calibrate <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-k">not</span> accept_tol:</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> run calibration</span></td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> skip_calibrate:</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.calibrate()</td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">            skip_calibrate <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> instantiate trackers</span></td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">            cut_list <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> store IDs that will be cut</span></td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">            nan_list <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> IDs of NaN to be cut immediately</span></td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">            full_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">            single_cut_idx <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">            tmp_max <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_diff_tol</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">            df_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> group by filter and perform comparison</span></td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> filt, group <span class="pl-k">in</span> <span class="pl-c1">self</span>.calibrators.groupby(<span class="pl-s"><span class="pl-pds">&#39;</span>Filter<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> use specific filters if specified</span></td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> filt <span class="pl-k">not</span> <span class="pl-k">in</span> use_filts:</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> if clear is not the only filter, skip it in comparison unless forced to use</span></td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.filters) <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>) <span class="pl-k">and</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.filters) <span class="pl-k">and</span> (filt <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> (<span class="pl-k">not</span> force_clear):</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">                df <span class="pl-k">=</span> group.median(<span class="pl-v">level</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">                df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>pct_im<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> group[<span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>].notnull().sum(<span class="pl-v">level</span><span class="pl-k">=</span><span class="pl-c1">1</span>) <span class="pl-k">/</span> <span class="pl-c1">len</span>(group[<span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>].groupby(<span class="pl-v">level</span><span class="pl-k">=</span><span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">                df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>std_obs<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> group.std(<span class="pl-v">level</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>).loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">                df <span class="pl-k">=</span> df.sort_index()</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">                df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_diff<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>] <span class="pl-k">-</span> df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_cal<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">                df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Diff<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> np.abs(df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_diff<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line">                cut_list.extend(<span class="pl-c1">list</span>(df.index[df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Diff<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&gt;</span> <span class="pl-c1">self</span>.cal_diff_tol]))</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">                nan_list.extend(<span class="pl-c1">list</span>(df.index[df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Diff<span class="pl-pds">&#39;</span></span>].isnull()]))</td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">len</span>(nan_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">                full_list <span class="pl-k">=</span> <span class="pl-c1">list</span>(df.index) <span class="pl-c"><span class="pl-c">#</span> ok to overwrite b/c same each time</span></td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Filter: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(filt))</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span>)</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(df.loc[:, [<span class="pl-s"><span class="pl-pds">&#39;</span>pct_im<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>RA_diff<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC_diff<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_cal<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>std_obs<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_diff<span class="pl-pds">&#39;</span></span>]].round(<span class="pl-c1">4</span>))</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> find index and value of maximum diff</span></td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">                    maxi <span class="pl-k">=</span> df.loc[:, <span class="pl-s"><span class="pl-pds">&#39;</span>Diff<span class="pl-pds">&#39;</span></span>].idxmax()</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">                    maxd <span class="pl-k">=</span> df.loc[maxi, <span class="pl-s"><span class="pl-pds">&#39;</span>Diff<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> maxd <span class="pl-k">&gt;</span> tmp_max:</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">                        single_cut_idx <span class="pl-k">=</span> maxi</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">                        tmp_max <span class="pl-k">=</span> maxd</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">                df.insert(<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Filter<span class="pl-pds">&#39;</span></span>, filt)</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">                df_list.append(df)</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line">            cut_list <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-c1">set</span>(cut_list))</td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> remove NaN</span></td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(nan_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>cutting IDs <span class="pl-c1">{}</span> for NaN<span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(i) <span class="pl-k">for</span> i <span class="pl-k">in</span> nan_list])))</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs.drop(nan_list)</td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> make cuts to refstars as needed</span></td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._display_refstars(<span class="pl-v">display</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span><span class="pl-k">*</span><span class="pl-c1">60</span>)</td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> warn if any individual images have too few ref stars</span></td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">                ref_counts <span class="pl-k">=</span> <span class="pl-c1">self</span>.calibrators[<span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>].notnull().sum(<span class="pl-v">level</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (ref_counts <span class="pl-k">&lt;</span> <span class="pl-c1">self</span>.min_ref_num).sum() <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Warning - the following images have below the minimum number of ref stars (<span class="pl-c1">{}</span>):<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.min_ref_num))</td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(ref_counts.index[ref_counts <span class="pl-k">&lt;</span> <span class="pl-c1">self</span>.min_ref_num])</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (ref_counts <span class="pl-k">==</span> <span class="pl-c1">self</span>.min_ref_num).sum() <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Warning - the following images have the minimum number of ref stars (<span class="pl-c1">{}</span>):<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.min_ref_num))</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(ref_counts.index[ref_counts <span class="pl-k">==</span> <span class="pl-c1">self</span>.min_ref_num])</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Do not cut the following IDs to avoid falling below the minimum:<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">                    idx_selector <span class="pl-k">=</span> (ref_counts.index[ref_counts <span class="pl-k">==</span> <span class="pl-c1">self</span>.min_ref_num], <span class="pl-c1">self</span>.cal_IDs)</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">                    num_affected <span class="pl-k">=</span> <span class="pl-c1">self</span>.calibrators.loc[idx_selector, <span class="pl-s"><span class="pl-pds">&#39;</span>Mag_obs<span class="pl-pds">&#39;</span></span>].notnull().sum(<span class="pl-v">level</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(num_affected.index[num_affected <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>].sort_values())</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>At tolerance <span class="pl-c1">{}</span>, <span class="pl-c1">{}</span> IDs (out of <span class="pl-c1">{}</span>) will be cut<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.cal_diff_tol, <span class="pl-c1">len</span>(cut_list), <span class="pl-c1">len</span>(full_list)))</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-c1">sorted</span>(cut_list))</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Accept cuts with tolerance of <span class="pl-c1">{}</span> mag ([y])? If not, enter new tolerance (or a comma-separated list of IDs to cut) &gt; <span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.cal_diff_tol))</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">                plt.ioff()</td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">                plt.close()</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (response <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> response.lower()):</td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs.drop(cut_list)</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">                    accept_tol <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> response:</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.cal_diff_tol <span class="pl-k">=</span> <span class="pl-c1">float</span>(response)</td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">                    skip_calibrate <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs.drop([<span class="pl-c1">int</span>(i) <span class="pl-k">for</span> i <span class="pl-k">in</span> response.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)])</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> single_cut_idx <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">                accept_tol <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">len</span>(full_list) <span class="pl-k">&gt;</span> <span class="pl-c1">self</span>.min_ref_num:</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>cutting ID <span class="pl-c1">{}</span> for exceeding tolerance and re-running calibration<span class="pl-pds">&#39;</span></span>.format(single_cut_idx))</td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs.drop([single_cut_idx])</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">self</span>.cal_diff_tol <span class="pl-k">&lt;=</span> <span class="pl-c1">self</span>.abs_cal_tol:</td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>increasing tolerance to <span class="pl-c1">{}</span> and re-running calibration<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.cal_diff_tol))</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.cal_diff_tol <span class="pl-k">+=</span> <span class="pl-c1">0.05</span></td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>calibration tolerance exceeds <span class="pl-c1">{}</span>, cannot proceed<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.abs_cal_tol))</td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.write_summary) <span class="pl-k">-</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-s"><span class="pl-pds">&#39;</span>final_ref_stars.dat<span class="pl-pds">&#39;</span></span>), <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">            outfile.write(pd.concat([df.loc[<span class="pl-c1">self</span>.cal_IDs, :] <span class="pl-k">for</span> df <span class="pl-k">in</span> df_list], <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).to_string())</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> make final pass on calibration to track failures and write .dat files</span></td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calibrate(<span class="pl-v">final_pass</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> write final &quot;use&quot; files</span></td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-c1">self</span>.calfile_use), <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">            outfile.write(<span class="pl-c1">self</span>.cal_use.loc[<span class="pl-c1">self</span>.cal_IDs, :].to_string(<span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>))</td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">        catalog <span class="pl-k">=</span> LPPu.astroCatalog(<span class="pl-c1">self</span>.targetname, <span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, <span class="pl-v">relative_path</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.calibration_dir)</td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">        catalog.cal_filename <span class="pl-k">=</span> <span class="pl-c1">self</span>.calfile_use</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        catalog.cal_source <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_source</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">        catalog.to_natural()</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> show new ref stars</span></td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">        plt.ioff()</td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._display_refstars()</td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_zeromag_all_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>get and set zeromag for every phot instance<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>getting zeromag for each image<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.get_zeromag())</td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_limmag_all_image</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>get and set limiting mag for every phot instance<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>getting limiting mag for each image<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].progress_apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.calc_limmag())</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_raw_lcs</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">color_term</span>, <span class="pl-smi">photsub_mode</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>builds raw light curve files from calibrated results<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">        columns <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>;; MJD<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>etburst<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>mag<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-emag<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>+emag<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>limmag<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>imagename<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">        lc <span class="pl-k">=</span> {name: [] <span class="pl-k">for</span> name <span class="pl-k">in</span> columns}</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">        lcs <span class="pl-k">=</span> {m: copy.deepcopy(lc) <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod}</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> iterate through files and extract LC information</span></td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> idx, img <span class="pl-k">in</span> <span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].iteritems():</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> immediately skip if not the appropriate color term unless being forced</span></td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (color_term <span class="pl-k">!=</span> img.color_term) <span class="pl-k">and</span> (<span class="pl-c1">self</span>.force_color_term <span class="pl-k">is</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> skip failed images</span></td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (idx <span class="pl-k">in</span> <span class="pl-c1">self</span>.cfIndex) <span class="pl-k">and</span> (photsub_mode <span class="pl-k">is</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> ((idx <span class="pl-k">in</span> <span class="pl-c1">self</span>.psfIndex) <span class="pl-k">or</span> (idx <span class="pl-k">in</span> <span class="pl-c1">self</span>.csfIndex)) <span class="pl-k">and</span> (photsub_mode <span class="pl-k">is</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> read photometry results</span></td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">            cols <span class="pl-k">=</span> (<span class="pl-c1">0</span>,) <span class="pl-k">+</span> <span class="pl-c1">sum</span>(((<span class="pl-c1">self</span>.phot_cols[m], <span class="pl-c1">self</span>.phot_cols[m] <span class="pl-k">+</span> <span class="pl-c1">1</span>) <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod), ())</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">            col_names <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>ID<span class="pl-pds">&#39;</span></span>,) <span class="pl-k">+</span> <span class="pl-c1">sum</span>(((m <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_mag<span class="pl-pds">&#39;</span></span>, m <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_err<span class="pl-pds">&#39;</span></span>) <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod), ())</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> photsub_mode <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">                dat <span class="pl-k">=</span> img.psfdat</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">                dat <span class="pl-k">=</span> img.psfsubdat</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">            d <span class="pl-k">=</span> pd.read_csv(dat, <span class="pl-v">header</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">comment</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>;<span class="pl-pds">&#39;</span></span>, <span class="pl-v">usecols</span><span class="pl-k">=</span>cols, <span class="pl-v">names</span> <span class="pl-k">=</span> col_names)</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> detect if no target in file</span></td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">not</span> <span class="pl-k">in</span> d[<span class="pl-s"><span class="pl-pds">&#39;</span>ID<span class="pl-pds">&#39;</span></span>].values:</td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>no object in calibrated photometry file: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(dat))</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> photsub_mode <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.noIndex.append(idx)</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.nosIndex.append(idx)</td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> setup columns for each raw file</span></td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod:</td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>;; MJD<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(img.mjd, <span class="pl-c1">6</span>))</td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>etburst<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(img.exptime <span class="pl-k">/</span> (<span class="pl-c1">60</span> <span class="pl-k">*</span> <span class="pl-c1">24</span>), <span class="pl-c1">5</span>)) <span class="pl-c"><span class="pl-c">#</span> exposure time in days</span></td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span>].append(img.filter.upper())</td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>imagename<span class="pl-pds">&#39;</span></span>].append(img.cimg)</td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>limmag<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(img.limmag, <span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">not</span> <span class="pl-k">in</span> d[<span class="pl-s"><span class="pl-pds">&#39;</span>ID<span class="pl-pds">&#39;</span></span>].values:</td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">                    mag <span class="pl-k">=</span> np.nan</td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line">                    err <span class="pl-k">=</span> np.nan</td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">                    mag <span class="pl-k">=</span> d[d[<span class="pl-s"><span class="pl-pds">&#39;</span>ID<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">1</span>][m <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_mag<span class="pl-pds">&#39;</span></span>].item()</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">                    err <span class="pl-k">=</span> d[d[<span class="pl-s"><span class="pl-pds">&#39;</span>ID<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">1</span>][m <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_err<span class="pl-pds">&#39;</span></span>].item()</td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>mag<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(mag,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>-emag<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(mag <span class="pl-k">-</span> err,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">                lcs[m][<span class="pl-s"><span class="pl-pds">&#39;</span>+emag<span class="pl-pds">&#39;</span></span>].append(<span class="pl-c1">round</span>(mag <span class="pl-k">+</span> err,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> write raw lc files</span></td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.photmethod:</td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line">            lc_raw_name <span class="pl-k">=</span> <span class="pl-c1">self</span>._lc_fname(color_term, m, <span class="pl-s"><span class="pl-pds">&#39;</span>raw<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> photsub_mode)</td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line">            lc_raw <span class="pl-k">=</span> pd.DataFrame(lcs[m])</td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line">            lc_raw.to_csv(lc_raw_name, <span class="pl-v">sep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">columns</span> <span class="pl-k">=</span> columns, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">na_rep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line">            p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc_raw_name, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line">            p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_bin_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">infile</span>, <span class="pl-smi">outfile</span>):</td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>wraps IDL lightcurve binning routine<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line">        idl_cmd <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>idl -e &quot;lpp_dat_res_bin, &#39;<span class="pl-c1">{}</span>&#39;, &#39;<span class="pl-c1">{}</span>&#39;, OUTFILE=&#39;<span class="pl-c1">{}</span>&#39;, /OUTPUT&quot;<span class="pl-pds">&#39;&#39;&#39;</span></span>.format(infile, outfile, outfile)</td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line">        stdout, stderr <span class="pl-k">=</span> LPPu.idl(idl_cmd)</td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._log_idl(idl_cmd, stdout, stderr)</td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_group_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">infile</span>, <span class="pl-smi">outfile</span>):</td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>wraps IDL lightcurve grouping routine<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line">        idl_cmd <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>idl -e &quot;lpp_dat_res_group, &#39;<span class="pl-c1">{}</span>&#39;, &#39;<span class="pl-c1">{}</span>&#39;, OUTFILE=&#39;<span class="pl-c1">{}</span>&#39;&quot;<span class="pl-pds">&#39;&#39;&#39;</span></span>.format(infile, outfile, outfile)</td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line">        stdout, stderr <span class="pl-k">=</span> LPPu.idl(idl_cmd)</td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._log_idl(idl_cmd, stdout, stderr)</td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_final_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">color_term</span>, <span class="pl-smi">infile</span>, <span class="pl-smi">outfile</span>):</td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>wraps IDL routine to convert from natural system<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line">        idl_cmd <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>idl -e &quot;lpp_invert_natural_stand_objonly, &#39;<span class="pl-c1">{}</span>&#39;, &#39;<span class="pl-c1">{}</span>&#39;, OUTFILE=&#39;<span class="pl-c1">{}</span>&#39;, /OUTPUT&quot;<span class="pl-pds">&#39;&#39;&#39;</span></span>.format(infile, color_term, outfile)</td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line">        stdout, stderr <span class="pl-k">=</span> LPPu.idl(idl_cmd)</td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._log_idl(idl_cmd, stdout, stderr)</td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">raw2standard_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">infile</span>):</td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>wrap intermediate steps that transform light curves from &quot;raw&quot; to &quot;standard&quot;<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> assign convenience variables</span></td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line">        tmp <span class="pl-k">=</span> infile.split(<span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line">        ct <span class="pl-k">=</span> tmp[tmp.index(<span class="pl-s"><span class="pl-pds">&#39;</span>natural<span class="pl-pds">&#39;</span></span>) <span class="pl-k">-</span> <span class="pl-c1">2</span>] <span class="pl-c"><span class="pl-c">#</span> get color term</span></td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> tmp[tmp.index(<span class="pl-s"><span class="pl-pds">&#39;</span>natural<span class="pl-pds">&#39;</span></span>) <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-c"><span class="pl-c">#</span> get phot aperture</span></td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line">        binfile <span class="pl-k">=</span> infile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>raw<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>bin<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line">        groupfile <span class="pl-k">=</span> binfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>bin<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line">        lc <span class="pl-k">=</span> groupfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>natural_group<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>standard<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> do intermediate light curve steps</span></td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.generate_bin_lc(infile, binfile)</td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.generate_group_lc(binfile, groupfile)</td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(groupfile):</td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>no groupfile generated, skipping<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1015" class="blob-num js-line-number" data-line-number="1015"></td>
        <td id="LC1015" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span>, <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1016" class="blob-num js-line-number" data-line-number="1016"></td>
        <td id="LC1016" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.generate_final_lc(ct, groupfile, lc)</td>
      </tr>
      <tr>
        <td id="L1017" class="blob-num js-line-number" data-line-number="1017"></td>
        <td id="LC1017" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(lc):</td>
      </tr>
      <tr>
        <td id="L1018" class="blob-num js-line-number" data-line-number="1018"></td>
        <td id="LC1018" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>no standard lc generated, skipping<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1019" class="blob-num js-line-number" data-line-number="1019"></td>
        <td id="LC1019" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span>, <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1020" class="blob-num js-line-number" data-line-number="1020"></td>
        <td id="LC1020" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1021" class="blob-num js-line-number" data-line-number="1021"></td>
        <td id="LC1021" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> plot</span></td>
      </tr>
      <tr>
        <td id="L1022" class="blob-num js-line-number" data-line-number="1022"></td>
        <td id="LC1022" class="blob-code blob-code-inner js-file-line">        p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L1023" class="blob-num js-line-number" data-line-number="1023"></td>
        <td id="LC1023" class="blob-code blob-code-inner js-file-line">        p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1024" class="blob-num js-line-number" data-line-number="1024"></td>
        <td id="LC1024" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1025" class="blob-num js-line-number" data-line-number="1025"></td>
        <td id="LC1025" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span>, <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1026" class="blob-num js-line-number" data-line-number="1026"></td>
        <td id="LC1026" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1027" class="blob-num js-line-number" data-line-number="1027"></td>
        <td id="LC1027" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">sub</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L1028" class="blob-num js-line-number" data-line-number="1028"></td>
        <td id="LC1028" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>performs all functions to transform image photometry into calibrated light curve of target<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1029" class="blob-num js-line-number" data-line-number="1029"></td>
        <td id="LC1029" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1030" class="blob-num js-line-number" data-line-number="1030"></td>
        <td id="LC1030" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>generating and plotting light curves (sub mode: <span class="pl-c1">{}</span>)<span class="pl-pds">&#39;</span></span>.format(sub))</td>
      </tr>
      <tr>
        <td id="L1031" class="blob-num js-line-number" data-line-number="1031"></td>
        <td id="LC1031" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1032" class="blob-num js-line-number" data-line-number="1032"></td>
        <td id="LC1032" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set up file system</span></td>
      </tr>
      <tr>
        <td id="L1033" class="blob-num js-line-number" data-line-number="1033"></td>
        <td id="LC1033" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.isdir(<span class="pl-c1">self</span>.lc_dir):</td>
      </tr>
      <tr>
        <td id="L1034" class="blob-num js-line-number" data-line-number="1034"></td>
        <td id="LC1034" class="blob-code blob-code-inner js-file-line">            os.makedirs(<span class="pl-c1">self</span>.lc_dir)</td>
      </tr>
      <tr>
        <td id="L1035" class="blob-num js-line-number" data-line-number="1035"></td>
        <td id="LC1035" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1036" class="blob-num js-line-number" data-line-number="1036"></td>
        <td id="LC1036" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> select only colors terms that are used</span></td>
      </tr>
      <tr>
        <td id="L1037" class="blob-num js-line-number" data-line-number="1037"></td>
        <td id="LC1037" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.color_terms_used <span class="pl-k">=</span> {key: <span class="pl-c1">self</span>.color_terms[key] <span class="pl-k">for</span> key <span class="pl-k">in</span> <span class="pl-c1">self</span>.color_terms.keys() <span class="pl-k">if</span> <span class="pl-c1">self</span>.color_terms[key] <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>}</td>
      </tr>
      <tr>
        <td id="L1038" class="blob-num js-line-number" data-line-number="1038"></td>
        <td id="LC1038" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1039" class="blob-num js-line-number" data-line-number="1039"></td>
        <td id="LC1039" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> generate raw light curves</span></td>
      </tr>
      <tr>
        <td id="L1040" class="blob-num js-line-number" data-line-number="1040"></td>
        <td id="LC1040" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>generating raw light curves for the following color terms: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.color_terms_used.keys())))</td>
      </tr>
      <tr>
        <td id="L1041" class="blob-num js-line-number" data-line-number="1041"></td>
        <td id="LC1041" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> ct <span class="pl-k">in</span> tqdm(<span class="pl-c1">self</span>.color_terms_used.keys()):</td>
      </tr>
      <tr>
        <td id="L1042" class="blob-num js-line-number" data-line-number="1042"></td>
        <td id="LC1042" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.generate_raw_lcs(ct, <span class="pl-v">photsub_mode</span> <span class="pl-k">=</span> sub)</td>
      </tr>
      <tr>
        <td id="L1043" class="blob-num js-line-number" data-line-number="1043"></td>
        <td id="LC1043" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1044" class="blob-num js-line-number" data-line-number="1044"></td>
        <td id="LC1044" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> generate intermediate and final light curves</span></td>
      </tr>
      <tr>
        <td id="L1045" class="blob-num js-line-number" data-line-number="1045"></td>
        <td id="LC1045" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>generating &quot;standard&quot; light curves<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1046" class="blob-num js-line-number" data-line-number="1046"></td>
        <td id="LC1046" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> m <span class="pl-k">in</span> tqdm(<span class="pl-c1">self</span>.photmethod):</td>
      </tr>
      <tr>
        <td id="L1047" class="blob-num js-line-number" data-line-number="1047"></td>
        <td id="LC1047" class="blob-code blob-code-inner js-file-line">            all_nat <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1048" class="blob-num js-line-number" data-line-number="1048"></td>
        <td id="LC1048" class="blob-code blob-code-inner js-file-line">            all_std <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1049" class="blob-num js-line-number" data-line-number="1049"></td>
        <td id="LC1049" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> ct <span class="pl-k">in</span> <span class="pl-c1">self</span>.color_terms_used.keys():</td>
      </tr>
      <tr>
        <td id="L1050" class="blob-num js-line-number" data-line-number="1050"></td>
        <td id="LC1050" class="blob-code blob-code-inner js-file-line">                group_succ, standard_succ <span class="pl-k">=</span> <span class="pl-c1">self</span>.raw2standard_lc(<span class="pl-c1">self</span>._lc_fname(ct, m, <span class="pl-s"><span class="pl-pds">&#39;</span>raw<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> sub))</td>
      </tr>
      <tr>
        <td id="L1051" class="blob-num js-line-number" data-line-number="1051"></td>
        <td id="LC1051" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> group_succ <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1052" class="blob-num js-line-number" data-line-number="1052"></td>
        <td id="LC1052" class="blob-code blob-code-inner js-file-line">                    all_nat.append((ct, <span class="pl-c1">self</span>._lc_fname(ct, m, <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> sub)))</td>
      </tr>
      <tr>
        <td id="L1053" class="blob-num js-line-number" data-line-number="1053"></td>
        <td id="LC1053" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> standard_succ <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1054" class="blob-num js-line-number" data-line-number="1054"></td>
        <td id="LC1054" class="blob-code blob-code-inner js-file-line">                    all_std.append(<span class="pl-c1">self</span>._lc_fname(ct, m, <span class="pl-s"><span class="pl-pds">&#39;</span>standard<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> sub))</td>
      </tr>
      <tr>
        <td id="L1055" class="blob-num js-line-number" data-line-number="1055"></td>
        <td id="LC1055" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> make &quot;all&quot; light curves</span></td>
      </tr>
      <tr>
        <td id="L1056" class="blob-num js-line-number" data-line-number="1056"></td>
        <td id="LC1056" class="blob-code blob-code-inner js-file-line">            lc_nat <span class="pl-k">=</span> <span class="pl-c1">self</span>._lc_fname(<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>, m, <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> sub)</td>
      </tr>
      <tr>
        <td id="L1057" class="blob-num js-line-number" data-line-number="1057"></td>
        <td id="LC1057" class="blob-code blob-code-inner js-file-line">            concat_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1058" class="blob-num js-line-number" data-line-number="1058"></td>
        <td id="LC1058" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> row <span class="pl-k">in</span> all_nat:</td>
      </tr>
      <tr>
        <td id="L1059" class="blob-num js-line-number" data-line-number="1059"></td>
        <td id="LC1059" class="blob-code blob-code-inner js-file-line">                tmp <span class="pl-k">=</span> pd.read_csv(row[<span class="pl-c1">1</span>], <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1060" class="blob-num js-line-number" data-line-number="1060"></td>
        <td id="LC1060" class="blob-code blob-code-inner js-file-line">                tmp.insert(<span class="pl-c1">3</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>SYSTEM<span class="pl-pds">&#39;</span></span>, row[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1061" class="blob-num js-line-number" data-line-number="1061"></td>
        <td id="LC1061" class="blob-code blob-code-inner js-file-line">                concat_list.append(tmp)</td>
      </tr>
      <tr>
        <td id="L1062" class="blob-num js-line-number" data-line-number="1062"></td>
        <td id="LC1062" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(concat_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1063" class="blob-num js-line-number" data-line-number="1063"></td>
        <td id="LC1063" class="blob-code blob-code-inner js-file-line">                pd.concat(concat_list, <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).to_csv(lc_nat, <span class="pl-v">sep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">na_rep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1064" class="blob-num js-line-number" data-line-number="1064"></td>
        <td id="LC1064" class="blob-code blob-code-inner js-file-line">                p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc_nat, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L1065" class="blob-num js-line-number" data-line-number="1065"></td>
        <td id="LC1065" class="blob-code blob-code-inner js-file-line">                p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1066" class="blob-num js-line-number" data-line-number="1066"></td>
        <td id="LC1066" class="blob-code blob-code-inner js-file-line">            lc <span class="pl-k">=</span> <span class="pl-c1">self</span>._lc_fname(<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>, m, <span class="pl-s"><span class="pl-pds">&#39;</span>standard<span class="pl-pds">&#39;</span></span>, <span class="pl-v">sub</span> <span class="pl-k">=</span> sub)</td>
      </tr>
      <tr>
        <td id="L1067" class="blob-num js-line-number" data-line-number="1067"></td>
        <td id="LC1067" class="blob-code blob-code-inner js-file-line">            concat_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1068" class="blob-num js-line-number" data-line-number="1068"></td>
        <td id="LC1068" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> fl <span class="pl-k">in</span> all_std:</td>
      </tr>
      <tr>
        <td id="L1069" class="blob-num js-line-number" data-line-number="1069"></td>
        <td id="LC1069" class="blob-code blob-code-inner js-file-line">                concat_list.append(pd.read_csv(fl, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>))</td>
      </tr>
      <tr>
        <td id="L1070" class="blob-num js-line-number" data-line-number="1070"></td>
        <td id="LC1070" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(concat_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1071" class="blob-num js-line-number" data-line-number="1071"></td>
        <td id="LC1071" class="blob-code blob-code-inner js-file-line">                pd.concat(concat_list, <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).to_csv(lc, <span class="pl-v">sep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">na_rep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1072" class="blob-num js-line-number" data-line-number="1072"></td>
        <td id="LC1072" class="blob-code blob-code-inner js-file-line">                p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L1073" class="blob-num js-line-number" data-line-number="1073"></td>
        <td id="LC1073" class="blob-code blob-code-inner js-file-line">                p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1074" class="blob-num js-line-number" data-line-number="1074"></td>
        <td id="LC1074" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1075" class="blob-num js-line-number" data-line-number="1075"></td>
        <td id="LC1075" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>done with light curves<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1076" class="blob-num js-line-number" data-line-number="1076"></td>
        <td id="LC1076" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.run_success <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1077" class="blob-num js-line-number" data-line-number="1077"></td>
        <td id="LC1077" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1078" class="blob-num js-line-number" data-line-number="1078"></td>
        <td id="LC1078" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> use recursion to handle sub if needed</span></td>
      </tr>
      <tr>
        <td id="L1079" class="blob-num js-line-number" data-line-number="1079"></td>
        <td id="LC1079" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-c1">self</span>.photsub <span class="pl-k">is</span> <span class="pl-c1">True</span>) <span class="pl-k">and</span> (sub <span class="pl-k">is</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L1080" class="blob-num js-line-number" data-line-number="1080"></td>
        <td id="LC1080" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.generate_lc(<span class="pl-v">sub</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1081" class="blob-num js-line-number" data-line-number="1081"></td>
        <td id="LC1081" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1082" class="blob-num js-line-number" data-line-number="1082"></td>
        <td id="LC1082" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">write_summary</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1083" class="blob-num js-line-number" data-line-number="1083"></td>
        <td id="LC1083" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>write summary file<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1084" class="blob-num js-line-number" data-line-number="1084"></td>
        <td id="LC1084" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1085" class="blob-num js-line-number" data-line-number="1085"></td>
        <td id="LC1085" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.current_step <span class="pl-k">!=</span> (<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.steps) <span class="pl-k">-</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L1086" class="blob-num js-line-number" data-line-number="1086"></td>
        <td id="LC1086" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>processing must be done before summary can be written<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1087" class="blob-num js-line-number" data-line-number="1087"></td>
        <td id="LC1087" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1088" class="blob-num js-line-number" data-line-number="1088"></td>
        <td id="LC1088" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1089" class="blob-num js-line-number" data-line-number="1089"></td>
        <td id="LC1089" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> get filters used</span></td>
      </tr>
      <tr>
        <td id="L1090" class="blob-num js-line-number" data-line-number="1090"></td>
        <td id="LC1090" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.filters <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.phot_instances.loc[<span class="pl-c1">self</span>.wIndex].apply(<span class="pl-k">lambda</span> <span class="pl-smi">img</span>: img.filter.upper()))</td>
      </tr>
      <tr>
        <td id="L1091" class="blob-num js-line-number" data-line-number="1091"></td>
        <td id="LC1091" class="blob-code blob-code-inner js-file-line">        ctu <span class="pl-k">=</span> <span class="pl-c1">self</span>.color_terms_used</td>
      </tr>
      <tr>
        <td id="L1092" class="blob-num js-line-number" data-line-number="1092"></td>
        <td id="LC1092" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> ctu <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1093" class="blob-num js-line-number" data-line-number="1093"></td>
        <td id="LC1093" class="blob-code blob-code-inner js-file-line">            ctu <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(ctu.keys())</td>
      </tr>
      <tr>
        <td id="L1094" class="blob-num js-line-number" data-line-number="1094"></td>
        <td id="LC1094" class="blob-code blob-code-inner js-file-line">        stars <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs</td>
      </tr>
      <tr>
        <td id="L1095" class="blob-num js-line-number" data-line-number="1095"></td>
        <td id="LC1095" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> stars <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1096" class="blob-num js-line-number" data-line-number="1096"></td>
        <td id="LC1096" class="blob-code blob-code-inner js-file-line">            stars <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.cal_IDs.astype(<span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L1097" class="blob-num js-line-number" data-line-number="1097"></td>
        <td id="LC1097" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1098" class="blob-num js-line-number" data-line-number="1098"></td>
        <td id="LC1098" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.summary_file <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.summary<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1099" class="blob-num js-line-number" data-line-number="1099"></td>
        <td id="LC1099" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.summary_file, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L1100" class="blob-num js-line-number" data-line-number="1100"></td>
        <td id="LC1100" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>targetname<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.targetname))</td>
      </tr>
      <tr>
        <td id="L1101" class="blob-num js-line-number" data-line-number="1101"></td>
        <td id="LC1101" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>photsub<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.photsub))</td>
      </tr>
      <tr>
        <td id="L1102" class="blob-num js-line-number" data-line-number="1102"></td>
        <td id="LC1102" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>filters<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.filters)))</td>
      </tr>
      <tr>
        <td id="L1103" class="blob-num js-line-number" data-line-number="1103"></td>
        <td id="LC1103" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>apertures<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.photmethod)))</td>
      </tr>
      <tr>
        <td id="L1104" class="blob-num js-line-number" data-line-number="1104"></td>
        <td id="LC1104" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>calmethod<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.calmethod))</td>
      </tr>
      <tr>
        <td id="L1105" class="blob-num js-line-number" data-line-number="1105"></td>
        <td id="LC1105" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>color_terms<span class="pl-pds">&#39;</span></span>, ctu))</td>
      </tr>
      <tr>
        <td id="L1106" class="blob-num js-line-number" data-line-number="1106"></td>
        <td id="LC1106" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num images<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.phot_instances)))</td>
      </tr>
      <tr>
        <td id="L1107" class="blob-num js-line-number" data-line-number="1107"></td>
        <td id="LC1107" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num failures<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.aIndex) <span class="pl-k">-</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.wIndex)))</td>
      </tr>
      <tr>
        <td id="L1108" class="blob-num js-line-number" data-line-number="1108"></td>
        <td id="LC1108" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num non-sup. filt.<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.bfIndex)))</td>
      </tr>
      <tr>
        <td id="L1109" class="blob-num js-line-number" data-line-number="1109"></td>
        <td id="LC1109" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num excl. by date<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.bdIndex)))</td>
      </tr>
      <tr>
        <td id="L1110" class="blob-num js-line-number" data-line-number="1110"></td>
        <td id="LC1110" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num phot failures<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.pfIndex)))</td>
      </tr>
      <tr>
        <td id="L1111" class="blob-num js-line-number" data-line-number="1111"></td>
        <td id="LC1111" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num cal failures<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.cfIndex)))</td>
      </tr>
      <tr>
        <td id="L1112" class="blob-num js-line-number" data-line-number="1112"></td>
        <td id="LC1112" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num no obj<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.noIndex)))</td>
      </tr>
      <tr>
        <td id="L1113" class="blob-num js-line-number" data-line-number="1113"></td>
        <td id="LC1113" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>num manually removed<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.mrIndex)))</td>
      </tr>
      <tr>
        <td id="L1114" class="blob-num js-line-number" data-line-number="1114"></td>
        <td id="LC1114" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>cal source<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.cal_source))</td>
      </tr>
      <tr>
        <td id="L1115" class="blob-num js-line-number" data-line-number="1115"></td>
        <td id="LC1115" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>cal stars<span class="pl-pds">&#39;</span></span>, stars))</td>
      </tr>
      <tr>
        <td id="L1116" class="blob-num js-line-number" data-line-number="1116"></td>
        <td id="LC1116" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>cal tolerance<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">round</span>(<span class="pl-c1">self</span>.cal_diff_tol, <span class="pl-c1">2</span>)))</td>
      </tr>
      <tr>
        <td id="L1117" class="blob-num js-line-number" data-line-number="1117"></td>
        <td id="LC1117" class="blob-code blob-code-inner js-file-line">            f.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{<span class="pl-k">:&lt;25</span>}{}</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-s"><span class="pl-pds">&#39;</span>run successful<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.run_success))</td>
      </tr>
      <tr>
        <td id="L1118" class="blob-num js-line-number" data-line-number="1118"></td>
        <td id="LC1118" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1119" class="blob-num js-line-number" data-line-number="1119"></td>
        <td id="LC1119" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>pipeline complete, summary file written<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1120" class="blob-num js-line-number" data-line-number="1120"></td>
        <td id="LC1120" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.save()</td>
      </tr>
      <tr>
        <td id="L1121" class="blob-num js-line-number" data-line-number="1121"></td>
        <td id="LC1121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1122" class="blob-num js-line-number" data-line-number="1122"></td>
        <td id="LC1122" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L1123" class="blob-num js-line-number" data-line-number="1123"></td>
        <td id="LC1123" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>          Utility Methods</span></td>
      </tr>
      <tr>
        <td id="L1124" class="blob-num js-line-number" data-line-number="1124"></td>
        <td id="LC1124" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L1125" class="blob-num js-line-number" data-line-number="1125"></td>
        <td id="LC1125" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1126" class="blob-num js-line-number" data-line-number="1126"></td>
        <td id="LC1126" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">manual_remove</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">id</span>):</td>
      </tr>
      <tr>
        <td id="L1127" class="blob-num js-line-number" data-line-number="1127"></td>
        <td id="LC1127" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>manually remove an index (or list of indices) from consideration<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1128" class="blob-num js-line-number" data-line-number="1128"></td>
        <td id="LC1128" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1129" class="blob-num js-line-number" data-line-number="1129"></td>
        <td id="LC1129" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(<span class="pl-c1">id</span>) <span class="pl-k">is</span> <span class="pl-c1">int</span>:</td>
      </tr>
      <tr>
        <td id="L1130" class="blob-num js-line-number" data-line-number="1130"></td>
        <td id="LC1130" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">id</span> <span class="pl-k">=</span> [<span class="pl-c1">id</span>]</td>
      </tr>
      <tr>
        <td id="L1131" class="blob-num js-line-number" data-line-number="1131"></td>
        <td id="LC1131" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">id</span> <span class="pl-k">=</span> pd.Index(<span class="pl-c1">id</span>)</td>
      </tr>
      <tr>
        <td id="L1132" class="blob-num js-line-number" data-line-number="1132"></td>
        <td id="LC1132" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mrIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.mrIndex.append(<span class="pl-c1">id</span>)</td>
      </tr>
      <tr>
        <td id="L1133" class="blob-num js-line-number" data-line-number="1133"></td>
        <td id="LC1133" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex.drop(<span class="pl-c1">id</span>)</td>
      </tr>
      <tr>
        <td id="L1134" class="blob-num js-line-number" data-line-number="1134"></td>
        <td id="LC1134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1135" class="blob-num js-line-number" data-line-number="1135"></td>
        <td id="LC1135" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">process_new_images</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">new_image_file</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">new_image_list</span> <span class="pl-k">=</span> []):</td>
      </tr>
      <tr>
        <td id="L1136" class="blob-num js-line-number" data-line-number="1136"></td>
        <td id="LC1136" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>processes images obtained after initial processing<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1137" class="blob-num js-line-number" data-line-number="1137"></td>
        <td id="LC1137" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1138" class="blob-num js-line-number" data-line-number="1138"></td>
        <td id="LC1138" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>processing new images<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1139" class="blob-num js-line-number" data-line-number="1139"></td>
        <td id="LC1139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1140" class="blob-num js-line-number" data-line-number="1140"></td>
        <td id="LC1140" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> read in new images to list</span></td>
      </tr>
      <tr>
        <td id="L1141" class="blob-num js-line-number" data-line-number="1141"></td>
        <td id="LC1141" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (new_image_file <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>) <span class="pl-k">and</span> (new_image_list <span class="pl-k">==</span> []):</td>
      </tr>
      <tr>
        <td id="L1142" class="blob-num js-line-number" data-line-number="1142"></td>
        <td id="LC1142" class="blob-code blob-code-inner js-file-line">            new_image_list <span class="pl-k">=</span> pd.read_csv(new_image_file, <span class="pl-v">header</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L1143" class="blob-num js-line-number" data-line-number="1143"></td>
        <td id="LC1143" class="blob-code blob-code-inner js-file-line">                                          <span class="pl-v">comment</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>, <span class="pl-v">squeeze</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1144" class="blob-num js-line-number" data-line-number="1144"></td>
        <td id="LC1144" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> new_image_list <span class="pl-k">!=</span> []:</td>
      </tr>
      <tr>
        <td id="L1145" class="blob-num js-line-number" data-line-number="1145"></td>
        <td id="LC1145" class="blob-code blob-code-inner js-file-line">            new_image_list <span class="pl-k">=</span> pd.Series(new_image_list)</td>
      </tr>
      <tr>
        <td id="L1146" class="blob-num js-line-number" data-line-number="1146"></td>
        <td id="LC1146" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1147" class="blob-num js-line-number" data-line-number="1147"></td>
        <td id="LC1147" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> remove any images from new list that have already been processed</span></td>
      </tr>
      <tr>
        <td id="L1148" class="blob-num js-line-number" data-line-number="1148"></td>
        <td id="LC1148" class="blob-code blob-code-inner js-file-line">        new_image_list <span class="pl-k">=</span> new_image_list[<span class="pl-k">~</span>new_image_list.isin(<span class="pl-c1">self</span>.image_list)]</td>
      </tr>
      <tr>
        <td id="L1149" class="blob-num js-line-number" data-line-number="1149"></td>
        <td id="LC1149" class="blob-code blob-code-inner js-file-line">        offset <span class="pl-k">=</span> <span class="pl-c1">self</span>.aIndex[<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L1150" class="blob-num js-line-number" data-line-number="1150"></td>
        <td id="LC1150" class="blob-code blob-code-inner js-file-line">        tmp <span class="pl-k">=</span> <span class="pl-c1">self</span>.wIndex</td>
      </tr>
      <tr>
        <td id="L1151" class="blob-num js-line-number" data-line-number="1151"></td>
        <td id="LC1151" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> pd.RangeIndex(<span class="pl-v">start</span> <span class="pl-k">=</span> offset, <span class="pl-v">stop</span> <span class="pl-k">=</span> offset <span class="pl-k">+</span> <span class="pl-c1">len</span>(new_image_list))</td>
      </tr>
      <tr>
        <td id="L1152" class="blob-num js-line-number" data-line-number="1152"></td>
        <td id="LC1152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1153" class="blob-num js-line-number" data-line-number="1153"></td>
        <td id="LC1153" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> only proceed if any images remain</span></td>
      </tr>
      <tr>
        <td id="L1154" class="blob-num js-line-number" data-line-number="1154"></td>
        <td id="LC1154" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(new_image_list) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1155" class="blob-num js-line-number" data-line-number="1155"></td>
        <td id="LC1155" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.warn(<span class="pl-s"><span class="pl-pds">&#39;</span>all images in new image list have already been processed, exiting<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1156" class="blob-num js-line-number" data-line-number="1156"></td>
        <td id="LC1156" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1157" class="blob-num js-line-number" data-line-number="1157"></td>
        <td id="LC1157" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1158" class="blob-num js-line-number" data-line-number="1158"></td>
        <td id="LC1158" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> update image list to include everything, and update phot_instances</span></td>
      </tr>
      <tr>
        <td id="L1159" class="blob-num js-line-number" data-line-number="1159"></td>
        <td id="LC1159" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>loading new images<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1160" class="blob-num js-line-number" data-line-number="1160"></td>
        <td id="LC1160" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.image_list <span class="pl-k">=</span> <span class="pl-c1">self</span>.image_list.append(new_image_list, <span class="pl-v">ignore_index</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1161" class="blob-num js-line-number" data-line-number="1161"></td>
        <td id="LC1161" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.append(<span class="pl-c1">self</span>._im2inst(new_image_list), <span class="pl-v">ignore_index</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1162" class="blob-num js-line-number" data-line-number="1162"></td>
        <td id="LC1162" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1163" class="blob-num js-line-number" data-line-number="1163"></td>
        <td id="LC1163" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> perform galaxy_subtraction and photometry on new images</span></td>
      </tr>
      <tr>
        <td id="L1164" class="blob-num js-line-number" data-line-number="1164"></td>
        <td id="LC1164" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.do_galaxy_subtraction_all_image()</td>
      </tr>
      <tr>
        <td id="L1165" class="blob-num js-line-number" data-line-number="1165"></td>
        <td id="LC1165" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.do_photometry_all_image()</td>
      </tr>
      <tr>
        <td id="L1166" class="blob-num js-line-number" data-line-number="1166"></td>
        <td id="LC1166" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.get_sky_all_image()</td>
      </tr>
      <tr>
        <td id="L1167" class="blob-num js-line-number" data-line-number="1167"></td>
        <td id="LC1167" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1168" class="blob-num js-line-number" data-line-number="1168"></td>
        <td id="LC1168" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> perform calibration</span></td>
      </tr>
      <tr>
        <td id="L1169" class="blob-num js-line-number" data-line-number="1169"></td>
        <td id="LC1169" class="blob-code blob-code-inner js-file-line">        full_cal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1170" class="blob-num js-line-number" data-line-number="1170"></td>
        <td id="LC1170" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L1171" class="blob-num js-line-number" data-line-number="1171"></td>
        <td id="LC1171" class="blob-code blob-code-inner js-file-line">            resp <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>perform full re-calibration? (y/[n]) &gt; <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1172" class="blob-num js-line-number" data-line-number="1172"></td>
        <td id="LC1172" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> resp.lower():</td>
      </tr>
      <tr>
        <td id="L1173" class="blob-num js-line-number" data-line-number="1173"></td>
        <td id="LC1173" class="blob-code blob-code-inner js-file-line">                full_cal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1174" class="blob-num js-line-number" data-line-number="1174"></td>
        <td id="LC1174" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> full_cal:</td>
      </tr>
      <tr>
        <td id="L1175" class="blob-num js-line-number" data-line-number="1175"></td>
        <td id="LC1175" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.do_calibration)</td>
      </tr>
      <tr>
        <td id="L1176" class="blob-num js-line-number" data-line-number="1176"></td>
        <td id="LC1176" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1177" class="blob-num js-line-number" data-line-number="1177"></td>
        <td id="LC1177" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.calibrate(<span class="pl-v">final_pass</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1178" class="blob-num js-line-number" data-line-number="1178"></td>
        <td id="LC1178" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.get_zeromag_all_image()</td>
      </tr>
      <tr>
        <td id="L1179" class="blob-num js-line-number" data-line-number="1179"></td>
        <td id="LC1179" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.get_limmag_all_image()</td>
      </tr>
      <tr>
        <td id="L1180" class="blob-num js-line-number" data-line-number="1180"></td>
        <td id="LC1180" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.current_step <span class="pl-k">=</span> <span class="pl-c1">self</span>.steps.index(<span class="pl-c1">self</span>.generate_lc)</td>
      </tr>
      <tr>
        <td id="L1181" class="blob-num js-line-number" data-line-number="1181"></td>
        <td id="LC1181" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1182" class="blob-num js-line-number" data-line-number="1182"></td>
        <td id="LC1182" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> run program after calibration has been completed (on all images)</span></td>
      </tr>
      <tr>
        <td id="L1183" class="blob-num js-line-number" data-line-number="1183"></td>
        <td id="LC1183" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.wIndex <span class="pl-k">=</span> tmp.append(<span class="pl-c1">self</span>.wIndex)</td>
      </tr>
      <tr>
        <td id="L1184" class="blob-num js-line-number" data-line-number="1184"></td>
        <td id="LC1184" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.run()</td>
      </tr>
      <tr>
        <td id="L1185" class="blob-num js-line-number" data-line-number="1185"></td>
        <td id="LC1185" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1186" class="blob-num js-line-number" data-line-number="1186"></td>
        <td id="LC1186" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> add to original image file and remove new file</span></td>
      </tr>
      <tr>
        <td id="L1187" class="blob-num js-line-number" data-line-number="1187"></td>
        <td id="LC1187" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> new_image_file <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1188" class="blob-num js-line-number" data-line-number="1188"></td>
        <td id="LC1188" class="blob-code blob-code-inner js-file-line">            ow <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1189" class="blob-num js-line-number" data-line-number="1189"></td>
        <td id="LC1189" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.interactive:</td>
      </tr>
      <tr>
        <td id="L1190" class="blob-num js-line-number" data-line-number="1190"></td>
        <td id="LC1190" class="blob-code blob-code-inner js-file-line">                resp <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>add <span class="pl-c1">{}</span> to <span class="pl-c1">{}</span> and then remove <span class="pl-c1">{}</span>? (y/[n]) &gt; <span class="pl-pds">&#39;</span></span>.format(new_image_file, <span class="pl-c1">self</span>.photlistfile, new_image_file))</td>
      </tr>
      <tr>
        <td id="L1191" class="blob-num js-line-number" data-line-number="1191"></td>
        <td id="LC1191" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> resp.lower():</td>
      </tr>
      <tr>
        <td id="L1192" class="blob-num js-line-number" data-line-number="1192"></td>
        <td id="LC1192" class="blob-code blob-code-inner js-file-line">                    ow <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1193" class="blob-num js-line-number" data-line-number="1193"></td>
        <td id="LC1193" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> ow:</td>
      </tr>
      <tr>
        <td id="L1194" class="blob-num js-line-number" data-line-number="1194"></td>
        <td id="LC1194" class="blob-code blob-code-inner js-file-line">                os.system(<span class="pl-s"><span class="pl-pds">&#39;</span>cat <span class="pl-c1">{}</span> &gt;&gt; <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(new_image_file, <span class="pl-c1">self</span>.photlistfile))</td>
      </tr>
      <tr>
        <td id="L1195" class="blob-num js-line-number" data-line-number="1195"></td>
        <td id="LC1195" class="blob-code blob-code-inner js-file-line">                os.system(<span class="pl-s"><span class="pl-pds">&#39;</span>rm <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(new_image_file))</td>
      </tr>
      <tr>
        <td id="L1196" class="blob-num js-line-number" data-line-number="1196"></td>
        <td id="LC1196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1197" class="blob-num js-line-number" data-line-number="1197"></td>
        <td id="LC1197" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>new images processed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1198" class="blob-num js-line-number" data-line-number="1198"></td>
        <td id="LC1198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1199" class="blob-num js-line-number" data-line-number="1199"></td>
        <td id="LC1199" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">load_templates</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1200" class="blob-num js-line-number" data-line-number="1200"></td>
        <td id="LC1200" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>search templates dir, setup, and convert formats as needed<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1201" class="blob-num js-line-number" data-line-number="1201"></td>
        <td id="LC1201" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1202" class="blob-num js-line-number" data-line-number="1202"></td>
        <td id="LC1202" class="blob-code blob-code-inner js-file-line">        succ <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1203" class="blob-num js-line-number" data-line-number="1203"></td>
        <td id="LC1203" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.template_images <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>_<span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(f, tel): <span class="pl-c1">None</span> <span class="pl-k">for</span> f <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> tel <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>kait<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>nickel<span class="pl-pds">&#39;</span></span>]}</td>
      </tr>
      <tr>
        <td id="L1204" class="blob-num js-line-number" data-line-number="1204"></td>
        <td id="LC1204" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR_kait<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">None</span> <span class="pl-c"><span class="pl-c">#</span> no clear for Nickel</span></td>
      </tr>
      <tr>
        <td id="L1205" class="blob-num js-line-number" data-line-number="1205"></td>
        <td id="LC1205" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1206" class="blob-num js-line-number" data-line-number="1206"></td>
        <td id="LC1206" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> os.path.exists(<span class="pl-c1">self</span>.templates_dir) <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L1207" class="blob-num js-line-number" data-line-number="1207"></td>
        <td id="LC1207" class="blob-code blob-code-inner js-file-line">            succ <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1208" class="blob-num js-line-number" data-line-number="1208"></td>
        <td id="LC1208" class="blob-code blob-code-inner js-file-line">            msg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>no templates directory, cannot do photsub<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1209" class="blob-num js-line-number" data-line-number="1209"></td>
        <td id="LC1209" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1210" class="blob-num js-line-number" data-line-number="1210"></td>
        <td id="LC1210" class="blob-code blob-code-inner js-file-line">            templates <span class="pl-k">=</span> glob.glob(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>/*c.fit<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.templates_dir))</td>
      </tr>
      <tr>
        <td id="L1211" class="blob-num js-line-number" data-line-number="1211"></td>
        <td id="LC1211" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(templates) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1212" class="blob-num js-line-number" data-line-number="1212"></td>
        <td id="LC1212" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>no templates available<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1213" class="blob-num js-line-number" data-line-number="1213"></td>
        <td id="LC1213" class="blob-code blob-code-inner js-file-line">                succ <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1214" class="blob-num js-line-number" data-line-number="1214"></td>
        <td id="LC1214" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1215" class="blob-num js-line-number" data-line-number="1215"></td>
        <td id="LC1215" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> succ <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1216" class="blob-num js-line-number" data-line-number="1216"></td>
        <td id="LC1216" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(templates) <span class="pl-k">&lt;</span> <span class="pl-c1">5</span>: <span class="pl-c"><span class="pl-c">#</span> 5 passbands</span></td>
      </tr>
      <tr>
        <td id="L1217" class="blob-num js-line-number" data-line-number="1217"></td>
        <td id="LC1217" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> warn if not enough templates found (but may be ok if not all needed)</span></td>
      </tr>
      <tr>
        <td id="L1218" class="blob-num js-line-number" data-line-number="1218"></td>
        <td id="LC1218" class="blob-code blob-code-inner js-file-line">                msg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>warning: did not find templates for every passband<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1219" class="blob-num js-line-number" data-line-number="1219"></td>
        <td id="LC1219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1220" class="blob-num js-line-number" data-line-number="1220"></td>
        <td id="LC1220" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> templ <span class="pl-k">in</span> templates:</td>
      </tr>
      <tr>
        <td id="L1221" class="blob-num js-line-number" data-line-number="1221"></td>
        <td id="LC1221" class="blob-code blob-code-inner js-file-line">                ti <span class="pl-k">=</span> FitsInfo(templ)</td>
      </tr>
      <tr>
        <td id="L1222" class="blob-num js-line-number" data-line-number="1222"></td>
        <td id="LC1222" class="blob-code blob-code-inner js-file-line">                filt <span class="pl-k">=</span> ti.filter.upper()</td>
      </tr>
      <tr>
        <td id="L1223" class="blob-num js-line-number" data-line-number="1223"></td>
        <td id="LC1223" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (ti.telescope.lower() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>nickel<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> (filt <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>n2k_c.fit<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> templ):</td>
      </tr>
      <tr>
        <td id="L1224" class="blob-num js-line-number" data-line-number="1224"></td>
        <td id="LC1224" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>_nickel<span class="pl-pds">&#39;</span></span>.format(filt)] <span class="pl-k">=</span> ti.cimg</td>
      </tr>
      <tr>
        <td id="L1225" class="blob-num js-line-number" data-line-number="1225"></td>
        <td id="LC1225" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> also rebin for kait</span></td>
      </tr>
      <tr>
        <td id="L1226" class="blob-num js-line-number" data-line-number="1226"></td>
        <td id="LC1226" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>_kait<span class="pl-pds">&#39;</span></span>.format(filt)] <span class="pl-k">=</span> ti.cimg.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>c.fit<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>n2k_c.fit<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1227" class="blob-num js-line-number" data-line-number="1227"></td>
        <td id="LC1227" class="blob-code blob-code-inner js-file-line">                    idl_cmd <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>idl -e &quot;lpp_rebin_nickel2kait, &#39;<span class="pl-c1">{}</span>&#39;, SAVEFILE=&#39;<span class="pl-c1">{}</span>&#39;&quot;<span class="pl-pds">&#39;&#39;&#39;</span></span>.format(ti.cimg, <span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>_kait<span class="pl-pds">&#39;</span></span>.format(filt)])</td>
      </tr>
      <tr>
        <td id="L1228" class="blob-num js-line-number" data-line-number="1228"></td>
        <td id="LC1228" class="blob-code blob-code-inner js-file-line">                    stdout, stderr <span class="pl-k">=</span> LPPu.idl(idl_cmd)</td>
      </tr>
      <tr>
        <td id="L1229" class="blob-num js-line-number" data-line-number="1229"></td>
        <td id="LC1229" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>._log_idl(idl_cmd, stdout, stderr)</td>
      </tr>
      <tr>
        <td id="L1230" class="blob-num js-line-number" data-line-number="1230"></td>
        <td id="LC1230" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(<span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>_kait<span class="pl-pds">&#39;</span></span>.format(filt)]):</td>
      </tr>
      <tr>
        <td id="L1231" class="blob-num js-line-number" data-line-number="1231"></td>
        <td id="LC1231" class="blob-code blob-code-inner js-file-line">                        succ <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1232" class="blob-num js-line-number" data-line-number="1232"></td>
        <td id="LC1232" class="blob-code blob-code-inner js-file-line">                        msg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>rebinning of templates from nickel to kait failed, cannot do photsub<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1233" class="blob-num js-line-number" data-line-number="1233"></td>
        <td id="LC1233" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> (ti.telescope.lower() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>kait<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> (filt <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>n2k_c.fit<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> templ):</td>
      </tr>
      <tr>
        <td id="L1234" class="blob-num js-line-number" data-line-number="1234"></td>
        <td id="LC1234" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.template_images[<span class="pl-s"><span class="pl-pds">&#39;</span>CLEAR_kait<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> ti.cimg</td>
      </tr>
      <tr>
        <td id="L1235" class="blob-num js-line-number" data-line-number="1235"></td>
        <td id="LC1235" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>n2k_c.fit<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> templ:</td>
      </tr>
      <tr>
        <td id="L1236" class="blob-num js-line-number" data-line-number="1236"></td>
        <td id="LC1236" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L1237" class="blob-num js-line-number" data-line-number="1237"></td>
        <td id="LC1237" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1238" class="blob-num js-line-number" data-line-number="1238"></td>
        <td id="LC1238" class="blob-code blob-code-inner js-file-line">                    succ <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1239" class="blob-num js-line-number" data-line-number="1239"></td>
        <td id="LC1239" class="blob-code blob-code-inner js-file-line">                    msg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>either BVRI templates are not from Nickel or CLEAR template is not from KAIT, cannnot do photsub<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1240" class="blob-num js-line-number" data-line-number="1240"></td>
        <td id="LC1240" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L1241" class="blob-num js-line-number" data-line-number="1241"></td>
        <td id="LC1241" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1242" class="blob-num js-line-number" data-line-number="1242"></td>
        <td id="LC1242" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> succ <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1243" class="blob-num js-line-number" data-line-number="1243"></td>
        <td id="LC1243" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>templates loaded<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1244" class="blob-num js-line-number" data-line-number="1244"></td>
        <td id="LC1244" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1245" class="blob-num js-line-number" data-line-number="1245"></td>
        <td id="LC1245" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1246" class="blob-num js-line-number" data-line-number="1246"></td>
        <td id="LC1246" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> otherwise process is not a success, search for candidates but proceed without photsub</span></td>
      </tr>
      <tr>
        <td id="L1247" class="blob-num js-line-number" data-line-number="1247"></td>
        <td id="LC1247" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.warning(msg)</td>
      </tr>
      <tr>
        <td id="L1248" class="blob-num js-line-number" data-line-number="1248"></td>
        <td id="LC1248" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.warning(<span class="pl-s"><span class="pl-pds">&#39;</span>switching to non-subtraction mode, but searching for template candidates<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1249" class="blob-num js-line-number" data-line-number="1249"></td>
        <td id="LC1249" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.template_images <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1250" class="blob-num js-line-number" data-line-number="1250"></td>
        <td id="LC1250" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.photsub <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1251" class="blob-num js-line-number" data-line-number="1251"></td>
        <td id="LC1251" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._get_template_candidates()</td>
      </tr>
      <tr>
        <td id="L1252" class="blob-num js-line-number" data-line-number="1252"></td>
        <td id="LC1252" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1253" class="blob-num js-line-number" data-line-number="1253"></td>
        <td id="LC1253" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_cal_info</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1254" class="blob-num js-line-number" data-line-number="1254"></td>
        <td id="LC1254" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>checks for existence of calibration files and writes them if found<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1255" class="blob-num js-line-number" data-line-number="1255"></td>
        <td id="LC1255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1256" class="blob-num js-line-number" data-line-number="1256"></td>
        <td id="LC1256" class="blob-code blob-code-inner js-file-line">        calfile <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cal_<span class="pl-c1">{}</span>_PS1.dat<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.targetname)</td>
      </tr>
      <tr>
        <td id="L1257" class="blob-num js-line-number" data-line-number="1257"></td>
        <td id="LC1257" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> os.path.exists(os.path.join(<span class="pl-c1">self</span>.calibration_dir, calfile)):</td>
      </tr>
      <tr>
        <td id="L1258" class="blob-num js-line-number" data-line-number="1258"></td>
        <td id="LC1258" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.calfile <span class="pl-k">=</span> calfile</td>
      </tr>
      <tr>
        <td id="L1259" class="blob-num js-line-number" data-line-number="1259"></td>
        <td id="LC1259" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>PS1<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1260" class="blob-num js-line-number" data-line-number="1260"></td>
        <td id="LC1260" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> os.path.exists(os.path.join(<span class="pl-c1">self</span>.calibration_dir, calfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>PS1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>SDSS<span class="pl-pds">&#39;</span></span>))):</td>
      </tr>
      <tr>
        <td id="L1261" class="blob-num js-line-number" data-line-number="1261"></td>
        <td id="LC1261" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.calfile <span class="pl-k">=</span> calfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>PS1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>SDSS<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1262" class="blob-num js-line-number" data-line-number="1262"></td>
        <td id="LC1262" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>SDSS<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1263" class="blob-num js-line-number" data-line-number="1263"></td>
        <td id="LC1263" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> os.path.exists(os.path.join(<span class="pl-c1">self</span>.calibration_dir, calfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>PS1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>APASS<span class="pl-pds">&#39;</span></span>))):</td>
      </tr>
      <tr>
        <td id="L1264" class="blob-num js-line-number" data-line-number="1264"></td>
        <td id="LC1264" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.calfile <span class="pl-k">=</span> calfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>PS1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>APASS<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1265" class="blob-num js-line-number" data-line-number="1265"></td>
        <td id="LC1265" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_source <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>APASS<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1266" class="blob-num js-line-number" data-line-number="1266"></td>
        <td id="LC1266" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.calfile_use <span class="pl-k">=</span> <span class="pl-c1">self</span>.calfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>.dat<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_use.dat<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1267" class="blob-num js-line-number" data-line-number="1267"></td>
        <td id="LC1267" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1268" class="blob-num js-line-number" data-line-number="1268"></td>
        <td id="LC1268" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">cut_lc_points</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">lc_file</span>, <span class="pl-smi">regenerate</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L1269" class="blob-num js-line-number" data-line-number="1269"></td>
        <td id="LC1269" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>interactively cut points from each band in input lc file<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1270" class="blob-num js-line-number" data-line-number="1270"></td>
        <td id="LC1270" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1271" class="blob-num js-line-number" data-line-number="1271"></td>
        <td id="LC1271" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>_all_<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> lc_file) <span class="pl-k">and</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>_raw<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> lc_file):</td>
      </tr>
      <tr>
        <td id="L1272" class="blob-num js-line-number" data-line-number="1272"></td>
        <td id="LC1272" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cut_raw_all_lc_points(lc_file)</td>
      </tr>
      <tr>
        <td id="L1273" class="blob-num js-line-number" data-line-number="1273"></td>
        <td id="LC1273" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1274" class="blob-num js-line-number" data-line-number="1274"></td>
        <td id="LC1274" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1275" class="blob-num js-line-number" data-line-number="1275"></td>
        <td id="LC1275" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>interactively cutting points from light curve file<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1276" class="blob-num js-line-number" data-line-number="1276"></td>
        <td id="LC1276" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1277" class="blob-num js-line-number" data-line-number="1277"></td>
        <td id="LC1277" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>working on <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(lc_file))</td>
      </tr>
      <tr>
        <td id="L1278" class="blob-num js-line-number" data-line-number="1278"></td>
        <td id="LC1278" class="blob-code blob-code-inner js-file-line">        p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc_file)</td>
      </tr>
      <tr>
        <td id="L1279" class="blob-num js-line-number" data-line-number="1279"></td>
        <td id="LC1279" class="blob-code blob-code-inner js-file-line">        p.plot_lc(<span class="pl-v">icut</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1280" class="blob-num js-line-number" data-line-number="1280"></td>
        <td id="LC1280" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1281" class="blob-num js-line-number" data-line-number="1281"></td>
        <td id="LC1281" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> regenerate <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1282" class="blob-num js-line-number" data-line-number="1282"></td>
        <td id="LC1282" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.raw2standard_lc(lc_file.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>.dat<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_cut.dat<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1283" class="blob-num js-line-number" data-line-number="1283"></td>
        <td id="LC1283" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1284" class="blob-num js-line-number" data-line-number="1284"></td>
        <td id="LC1284" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">cut_raw_all_lc_points</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">infile</span>):</td>
      </tr>
      <tr>
        <td id="L1285" class="blob-num js-line-number" data-line-number="1285"></td>
        <td id="LC1285" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>given &quot;all&quot; raw filename (need not exist), do cutting on relevant raw files and regenerate &quot;all&quot; files<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1286" class="blob-num js-line-number" data-line-number="1286"></td>
        <td id="LC1286" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1287" class="blob-num js-line-number" data-line-number="1287"></td>
        <td id="LC1287" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> assign convenience variables</span></td>
      </tr>
      <tr>
        <td id="L1288" class="blob-num js-line-number" data-line-number="1288"></td>
        <td id="LC1288" class="blob-code blob-code-inner js-file-line">        tmp <span class="pl-k">=</span> infile.split(<span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1289" class="blob-num js-line-number" data-line-number="1289"></td>
        <td id="LC1289" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> tmp[tmp.index(<span class="pl-s"><span class="pl-pds">&#39;</span>natural<span class="pl-pds">&#39;</span></span>) <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-c"><span class="pl-c">#</span> get phot aperture</span></td>
      </tr>
      <tr>
        <td id="L1290" class="blob-num js-line-number" data-line-number="1290"></td>
        <td id="LC1290" class="blob-code blob-code-inner js-file-line">        groupfile <span class="pl-k">=</span> infile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>raw<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>group<span class="pl-pds">&#39;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span>.dat<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_cut.dat<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1291" class="blob-num js-line-number" data-line-number="1291"></td>
        <td id="LC1291" class="blob-code blob-code-inner js-file-line">        lc <span class="pl-k">=</span> groupfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>natural_group<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>standard<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1292" class="blob-num js-line-number" data-line-number="1292"></td>
        <td id="LC1292" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1293" class="blob-num js-line-number" data-line-number="1293"></td>
        <td id="LC1293" class="blob-code blob-code-inner js-file-line">        all_nat <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1294" class="blob-num js-line-number" data-line-number="1294"></td>
        <td id="LC1294" class="blob-code blob-code-inner js-file-line">        all_std <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1295" class="blob-num js-line-number" data-line-number="1295"></td>
        <td id="LC1295" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> ct <span class="pl-k">in</span> <span class="pl-c1">self</span>.color_terms.keys():</td>
      </tr>
      <tr>
        <td id="L1296" class="blob-num js-line-number" data-line-number="1296"></td>
        <td id="LC1296" class="blob-code blob-code-inner js-file-line">            raw <span class="pl-k">=</span> infile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>, ct)</td>
      </tr>
      <tr>
        <td id="L1297" class="blob-num js-line-number" data-line-number="1297"></td>
        <td id="LC1297" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> os.path.exists(raw):</td>
      </tr>
      <tr>
        <td id="L1298" class="blob-num js-line-number" data-line-number="1298"></td>
        <td id="LC1298" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.cut_lc_points(raw, <span class="pl-v">regenerate</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1299" class="blob-num js-line-number" data-line-number="1299"></td>
        <td id="LC1299" class="blob-code blob-code-inner js-file-line">                all_nat.append((ct, groupfile.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>, ct)))</td>
      </tr>
      <tr>
        <td id="L1300" class="blob-num js-line-number" data-line-number="1300"></td>
        <td id="LC1300" class="blob-code blob-code-inner js-file-line">                all_std.append(lc.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>, ct))</td>
      </tr>
      <tr>
        <td id="L1301" class="blob-num js-line-number" data-line-number="1301"></td>
        <td id="LC1301" class="blob-code blob-code-inner js-file-line">        concat_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1302" class="blob-num js-line-number" data-line-number="1302"></td>
        <td id="LC1302" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> row <span class="pl-k">in</span> all_nat:</td>
      </tr>
      <tr>
        <td id="L1303" class="blob-num js-line-number" data-line-number="1303"></td>
        <td id="LC1303" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> os.path.exists(row[<span class="pl-c1">1</span>]):</td>
      </tr>
      <tr>
        <td id="L1304" class="blob-num js-line-number" data-line-number="1304"></td>
        <td id="LC1304" class="blob-code blob-code-inner js-file-line">                tmp <span class="pl-k">=</span> pd.read_csv(row[<span class="pl-c1">1</span>], <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1305" class="blob-num js-line-number" data-line-number="1305"></td>
        <td id="LC1305" class="blob-code blob-code-inner js-file-line">                tmp.insert(<span class="pl-c1">3</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>SYSTEM<span class="pl-pds">&#39;</span></span>, row[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1306" class="blob-num js-line-number" data-line-number="1306"></td>
        <td id="LC1306" class="blob-code blob-code-inner js-file-line">                concat_list.append(tmp)</td>
      </tr>
      <tr>
        <td id="L1307" class="blob-num js-line-number" data-line-number="1307"></td>
        <td id="LC1307" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(concat_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1308" class="blob-num js-line-number" data-line-number="1308"></td>
        <td id="LC1308" class="blob-code blob-code-inner js-file-line">            pd.concat(concat_list, <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).to_csv(groupfile, <span class="pl-v">sep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">na_rep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1309" class="blob-num js-line-number" data-line-number="1309"></td>
        <td id="LC1309" class="blob-code blob-code-inner js-file-line">            p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> groupfile, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L1310" class="blob-num js-line-number" data-line-number="1310"></td>
        <td id="LC1310" class="blob-code blob-code-inner js-file-line">            p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1311" class="blob-num js-line-number" data-line-number="1311"></td>
        <td id="LC1311" class="blob-code blob-code-inner js-file-line">        concat_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1312" class="blob-num js-line-number" data-line-number="1312"></td>
        <td id="LC1312" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> fl <span class="pl-k">in</span> all_std:</td>
      </tr>
      <tr>
        <td id="L1313" class="blob-num js-line-number" data-line-number="1313"></td>
        <td id="LC1313" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> os.path.exists(fl):</td>
      </tr>
      <tr>
        <td id="L1314" class="blob-num js-line-number" data-line-number="1314"></td>
        <td id="LC1314" class="blob-code blob-code-inner js-file-line">                concat_list.append(pd.read_csv(fl, <span class="pl-v">delim_whitespace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>))</td>
      </tr>
      <tr>
        <td id="L1315" class="blob-num js-line-number" data-line-number="1315"></td>
        <td id="LC1315" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(concat_list) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1316" class="blob-num js-line-number" data-line-number="1316"></td>
        <td id="LC1316" class="blob-code blob-code-inner js-file-line">            pd.concat(concat_list, <span class="pl-v">sort</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>).to_csv(lc, <span class="pl-v">sep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">na_rep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1317" class="blob-num js-line-number" data-line-number="1317"></td>
        <td id="LC1317" class="blob-code blob-code-inner js-file-line">            p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> lc, <span class="pl-v">name</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.targetname, <span class="pl-v">photmethod</span> <span class="pl-k">=</span> m)</td>
      </tr>
      <tr>
        <td id="L1318" class="blob-num js-line-number" data-line-number="1318"></td>
        <td id="LC1318" class="blob-code blob-code-inner js-file-line">            p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1319" class="blob-num js-line-number" data-line-number="1319"></td>
        <td id="LC1319" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1320" class="blob-num js-line-number" data-line-number="1320"></td>
        <td id="LC1320" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_lc</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">lc_list</span>):</td>
      </tr>
      <tr>
        <td id="L1321" class="blob-num js-line-number" data-line-number="1321"></td>
        <td id="LC1321" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>plots each light curve from the input list<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1322" class="blob-num js-line-number" data-line-number="1322"></td>
        <td id="LC1322" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1323" class="blob-num js-line-number" data-line-number="1323"></td>
        <td id="LC1323" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> fl <span class="pl-k">in</span> lc_list:</td>
      </tr>
      <tr>
        <td id="L1324" class="blob-num js-line-number" data-line-number="1324"></td>
        <td id="LC1324" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>plotting <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(fl))</td>
      </tr>
      <tr>
        <td id="L1325" class="blob-num js-line-number" data-line-number="1325"></td>
        <td id="LC1325" class="blob-code blob-code-inner js-file-line">            p <span class="pl-k">=</span> LPPu.plotLC(<span class="pl-v">lc_file</span> <span class="pl-k">=</span> fl)</td>
      </tr>
      <tr>
        <td id="L1326" class="blob-num js-line-number" data-line-number="1326"></td>
        <td id="LC1326" class="blob-code blob-code-inner js-file-line">            p.plot_lc(<span class="pl-v">extensions</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>.ps<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.png<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1327" class="blob-num js-line-number" data-line-number="1327"></td>
        <td id="LC1327" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1328" class="blob-num js-line-number" data-line-number="1328"></td>
        <td id="LC1328" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_ct2cf</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">color_term</span>, <span class="pl-smi">use</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L1329" class="blob-num js-line-number" data-line-number="1329"></td>
        <td id="LC1329" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>return &quot;calfit&quot; filename associated with input color term<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1330" class="blob-num js-line-number" data-line-number="1330"></td>
        <td id="LC1330" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1331" class="blob-num js-line-number" data-line-number="1331"></td>
        <td id="LC1331" class="blob-code blob-code-inner js-file-line">        base <span class="pl-k">=</span> <span class="pl-c1">self</span>.calfile.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L1332" class="blob-num js-line-number" data-line-number="1332"></td>
        <td id="LC1332" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> color_term <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Landolt<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1333" class="blob-num js-line-number" data-line-number="1333"></td>
        <td id="LC1333" class="blob-code blob-code-inner js-file-line">            cal_nat_fit <span class="pl-k">=</span> base <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-c1">{}</span>_natural.fit<span class="pl-pds">&#39;</span></span>.format(color_term)</td>
      </tr>
      <tr>
        <td id="L1334" class="blob-num js-line-number" data-line-number="1334"></td>
        <td id="LC1334" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1335" class="blob-num js-line-number" data-line-number="1335"></td>
        <td id="LC1335" class="blob-code blob-code-inner js-file-line">            cal_nat_fit <span class="pl-k">=</span> base <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_Landolt_standard.fit<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1336" class="blob-num js-line-number" data-line-number="1336"></td>
        <td id="LC1336" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> use <span class="pl-k">is</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L1337" class="blob-num js-line-number" data-line-number="1337"></td>
        <td id="LC1337" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> cal_nat_fit</td>
      </tr>
      <tr>
        <td id="L1338" class="blob-num js-line-number" data-line-number="1338"></td>
        <td id="LC1338" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1339" class="blob-num js-line-number" data-line-number="1339"></td>
        <td id="LC1339" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> cal_nat_fit.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-c1">{}</span>_<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.cal_source), <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-c1">{}</span>_use_<span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">self</span>.cal_source))</td>
      </tr>
      <tr>
        <td id="L1340" class="blob-num js-line-number" data-line-number="1340"></td>
        <td id="LC1340" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1341" class="blob-num js-line-number" data-line-number="1341"></td>
        <td id="LC1341" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_im2inst</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">image_list</span>, <span class="pl-smi">mode</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>progress<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L1342" class="blob-num js-line-number" data-line-number="1342"></td>
        <td id="LC1342" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>create a series of Phot instances from input image list (also a series)<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1343" class="blob-num js-line-number" data-line-number="1343"></td>
        <td id="LC1343" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1344" class="blob-num js-line-number" data-line-number="1344"></td>
        <td id="LC1344" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> hide astropy warnings</span></td>
      </tr>
      <tr>
        <td id="L1345" class="blob-num js-line-number" data-line-number="1345"></td>
        <td id="LC1345" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> warnings.catch_warnings():</td>
      </tr>
      <tr>
        <td id="L1346" class="blob-num js-line-number" data-line-number="1346"></td>
        <td id="LC1346" class="blob-code blob-code-inner js-file-line">            warnings.simplefilter(<span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span>, AstropyWarning)</td>
      </tr>
      <tr>
        <td id="L1347" class="blob-num js-line-number" data-line-number="1347"></td>
        <td id="LC1347" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> mode <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>quiet<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1348" class="blob-num js-line-number" data-line-number="1348"></td>
        <td id="LC1348" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> image_list.progress_apply(Phot, <span class="pl-v">radec</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.radec, <span class="pl-v">wdir</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.wdir)</td>
      </tr>
      <tr>
        <td id="L1349" class="blob-num js-line-number" data-line-number="1349"></td>
        <td id="LC1349" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1350" class="blob-num js-line-number" data-line-number="1350"></td>
        <td id="LC1350" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> image_list.apply(Phot, <span class="pl-v">radec</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.radec, <span class="pl-v">wdir</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.wdir)</td>
      </tr>
      <tr>
        <td id="L1351" class="blob-num js-line-number" data-line-number="1351"></td>
        <td id="LC1351" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1352" class="blob-num js-line-number" data-line-number="1352"></td>
        <td id="LC1352" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_lc_fname</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cterm</span>, <span class="pl-smi">pmethod</span>, <span class="pl-smi">lc_type</span>, <span class="pl-smi">sub</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L1353" class="blob-num js-line-number" data-line-number="1353"></td>
        <td id="LC1353" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>return light curve filename<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1354" class="blob-num js-line-number" data-line-number="1354"></td>
        <td id="LC1354" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1355" class="blob-num js-line-number" data-line-number="1355"></td>
        <td id="LC1355" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.lc_base <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1356" class="blob-num js-line-number" data-line-number="1356"></td>
        <td id="LC1356" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>set lc_base first<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1357" class="blob-num js-line-number" data-line-number="1357"></td>
        <td id="LC1357" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1358" class="blob-num js-line-number" data-line-number="1358"></td>
        <td id="LC1358" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1359" class="blob-num js-line-number" data-line-number="1359"></td>
        <td id="LC1359" class="blob-code blob-code-inner js-file-line">        full_base <span class="pl-k">=</span> <span class="pl-c1">self</span>.lc_base <span class="pl-k">+</span> cterm <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> pmethod</td>
      </tr>
      <tr>
        <td id="L1360" class="blob-num js-line-number" data-line-number="1360"></td>
        <td id="LC1360" class="blob-code blob-code-inner js-file-line">        lc_fname <span class="pl-k">=</span> full_base <span class="pl-k">+</span> <span class="pl-c1">self</span>.lc_ext[lc_type]</td>
      </tr>
      <tr>
        <td id="L1361" class="blob-num js-line-number" data-line-number="1361"></td>
        <td id="LC1361" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> sub <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1362" class="blob-num js-line-number" data-line-number="1362"></td>
        <td id="LC1362" class="blob-code blob-code-inner js-file-line">            lc_fname <span class="pl-k">=</span> lc_fname.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>.dat<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_sub.dat<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1363" class="blob-num js-line-number" data-line-number="1363"></td>
        <td id="LC1363" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1364" class="blob-num js-line-number" data-line-number="1364"></td>
        <td id="LC1364" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> lc_fname</td>
      </tr>
      <tr>
        <td id="L1365" class="blob-num js-line-number" data-line-number="1365"></td>
        <td id="LC1365" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1366" class="blob-num js-line-number" data-line-number="1366"></td>
        <td id="LC1366" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_get_template_candidates</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1367" class="blob-num js-line-number" data-line-number="1367"></td>
        <td id="LC1367" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>wrap LPPu function to get template candidates<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1368" class="blob-num js-line-number" data-line-number="1368"></td>
        <td id="LC1368" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1369" class="blob-num js-line-number" data-line-number="1369"></td>
        <td id="LC1369" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(<span class="pl-s"><span class="pl-pds">&#39;</span>searching for galaxy subtraction template images<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1370" class="blob-num js-line-number" data-line-number="1370"></td>
        <td id="LC1370" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1371" class="blob-num js-line-number" data-line-number="1371"></td>
        <td id="LC1371" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> fall back on first obs date if don&#39;t know discovery date</span></td>
      </tr>
      <tr>
        <td id="L1372" class="blob-num js-line-number" data-line-number="1372"></td>
        <td id="LC1372" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.disc_date_mjd <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1373" class="blob-num js-line-number" data-line-number="1373"></td>
        <td id="LC1373" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.first_obs <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1374" class="blob-num js-line-number" data-line-number="1374"></td>
        <td id="LC1374" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.first_obs <span class="pl-k">=</span> LPPu.get_first_obs_date(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L1375" class="blob-num js-line-number" data-line-number="1375"></td>
        <td id="LC1375" class="blob-code blob-code-inner js-file-line">            dt <span class="pl-k">=</span> <span class="pl-c1">self</span>.first_obs</td>
      </tr>
      <tr>
        <td id="L1376" class="blob-num js-line-number" data-line-number="1376"></td>
        <td id="LC1376" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1377" class="blob-num js-line-number" data-line-number="1377"></td>
        <td id="LC1377" class="blob-code blob-code-inner js-file-line">            dt <span class="pl-k">=</span> <span class="pl-c1">self</span>.disc_date_mjd</td>
      </tr>
      <tr>
        <td id="L1378" class="blob-num js-line-number" data-line-number="1378"></td>
        <td id="LC1378" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1379" class="blob-num js-line-number" data-line-number="1379"></td>
        <td id="LC1379" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">=</span> LPPu.get_template_candidates(<span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, dt, <span class="pl-c1">self</span>.templates_dir)</td>
      </tr>
      <tr>
        <td id="L1380" class="blob-num js-line-number" data-line-number="1380"></td>
        <td id="LC1380" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.info(result)</td>
      </tr>
      <tr>
        <td id="L1381" class="blob-num js-line-number" data-line-number="1381"></td>
        <td id="LC1381" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1382" class="blob-num js-line-number" data-line-number="1382"></td>
        <td id="LC1382" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_log_idl</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">idl_cmd</span>, <span class="pl-smi">stdout</span>, <span class="pl-smi">stderr</span>):</td>
      </tr>
      <tr>
        <td id="L1383" class="blob-num js-line-number" data-line-number="1383"></td>
        <td id="LC1383" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>log info regarding external idl calls<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1384" class="blob-num js-line-number" data-line-number="1384"></td>
        <td id="LC1384" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1385" class="blob-num js-line-number" data-line-number="1385"></td>
        <td id="LC1385" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>output of IDL command: <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(idl_cmd))</td>
      </tr>
      <tr>
        <td id="L1386" class="blob-num js-line-number" data-line-number="1386"></td>
        <td id="LC1386" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>STDOUT----<span class="pl-cce">\n</span><span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(stdout))</td>
      </tr>
      <tr>
        <td id="L1387" class="blob-num js-line-number" data-line-number="1387"></td>
        <td id="LC1387" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.log.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>STDERR----<span class="pl-cce">\n</span><span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(stderr))</td>
      </tr>
      <tr>
        <td id="L1388" class="blob-num js-line-number" data-line-number="1388"></td>
        <td id="LC1388" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1389" class="blob-num js-line-number" data-line-number="1389"></td>
        <td id="LC1389" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_display_refstars</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">icut</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">display</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">ax</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1390" class="blob-num js-line-number" data-line-number="1390"></td>
        <td id="LC1390" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>show reference image and plot selected reference stars<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1391" class="blob-num js-line-number" data-line-number="1391"></td>
        <td id="LC1391" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1392" class="blob-num js-line-number" data-line-number="1392"></td>
        <td id="LC1392" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">onpick</span>(<span class="pl-smi">event</span>, <span class="pl-smi">cut_list</span>, <span class="pl-smi">ref</span>, <span class="pl-smi">refp</span>, <span class="pl-smi">fig</span>):</td>
      </tr>
      <tr>
        <td id="L1393" class="blob-num js-line-number" data-line-number="1393"></td>
        <td id="LC1393" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>get index, append appropriate index to cut_list and remove star<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1394" class="blob-num js-line-number" data-line-number="1394"></td>
        <td id="LC1394" class="blob-code blob-code-inner js-file-line">            ind <span class="pl-k">=</span> event.ind[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L1395" class="blob-num js-line-number" data-line-number="1395"></td>
        <td id="LC1395" class="blob-code blob-code-inner js-file-line">            cut_list.append(ref.index.drop(cut_list)[ind])</td>
      </tr>
      <tr>
        <td id="L1396" class="blob-num js-line-number" data-line-number="1396"></td>
        <td id="LC1396" class="blob-code blob-code-inner js-file-line">            refp.set_data(ref.loc[ref.index.drop(cut_list), <span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>], ref.loc[ref.index.drop(cut_list), <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1397" class="blob-num js-line-number" data-line-number="1397"></td>
        <td id="LC1397" class="blob-code blob-code-inner js-file-line">            fig.canvas.draw()</td>
      </tr>
      <tr>
        <td id="L1398" class="blob-num js-line-number" data-line-number="1398"></td>
        <td id="LC1398" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1399" class="blob-num js-line-number" data-line-number="1399"></td>
        <td id="LC1399" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> set calibration IDs if necessary</span></td>
      </tr>
      <tr>
        <td id="L1400" class="blob-num js-line-number" data-line-number="1400"></td>
        <td id="LC1400" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1401" class="blob-num js-line-number" data-line-number="1401"></td>
        <td id="LC1401" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_use.index</td>
      </tr>
      <tr>
        <td id="L1402" class="blob-num js-line-number" data-line-number="1402"></td>
        <td id="LC1402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1403" class="blob-num js-line-number" data-line-number="1403"></td>
        <td id="LC1403" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> read needed information from image</span></td>
      </tr>
      <tr>
        <td id="L1404" class="blob-num js-line-number" data-line-number="1404"></td>
        <td id="LC1404" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> fits.open(<span class="pl-c1">self</span>.refname) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L1405" class="blob-num js-line-number" data-line-number="1405"></td>
        <td id="LC1405" class="blob-code blob-code-inner js-file-line">            im <span class="pl-k">=</span> f[<span class="pl-c1">0</span>].data</td>
      </tr>
      <tr>
        <td id="L1406" class="blob-num js-line-number" data-line-number="1406"></td>
        <td id="LC1406" class="blob-code blob-code-inner js-file-line">            head <span class="pl-k">=</span> f[<span class="pl-c1">0</span>].header</td>
      </tr>
      <tr>
        <td id="L1407" class="blob-num js-line-number" data-line-number="1407"></td>
        <td id="LC1407" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1408" class="blob-num js-line-number" data-line-number="1408"></td>
        <td id="LC1408" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> find pixel locations of sn, reference stars, and radec stars</span></td>
      </tr>
      <tr>
        <td id="L1409" class="blob-num js-line-number" data-line-number="1409"></td>
        <td id="LC1409" class="blob-code blob-code-inner js-file-line">        cs <span class="pl-k">=</span> WCS(<span class="pl-v">header</span> <span class="pl-k">=</span> head)</td>
      </tr>
      <tr>
        <td id="L1410" class="blob-num js-line-number" data-line-number="1410"></td>
        <td id="LC1410" class="blob-code blob-code-inner js-file-line">        sn_x, sn_y <span class="pl-k">=</span> cs.all_world2pix(<span class="pl-c1">self</span>.targetra, <span class="pl-c1">self</span>.targetdec, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L1411" class="blob-num js-line-number" data-line-number="1411"></td>
        <td id="LC1411" class="blob-code blob-code-inner js-file-line">        ref_x, ref_y <span class="pl-k">=</span> cs.all_world2pix(<span class="pl-c1">self</span>.cal_use.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>ra<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">self</span>.cal_use.loc[<span class="pl-c1">self</span>.cal_IDs, <span class="pl-s"><span class="pl-pds">&#39;</span>dec<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L1412" class="blob-num js-line-number" data-line-number="1412"></td>
        <td id="LC1412" class="blob-code blob-code-inner js-file-line">        ref <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>: ref_x, <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>: ref_y}, <span class="pl-v">index</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs)</td>
      </tr>
      <tr>
        <td id="L1413" class="blob-num js-line-number" data-line-number="1413"></td>
        <td id="LC1413" class="blob-code blob-code-inner js-file-line">        rd_x, rd_y <span class="pl-k">=</span> cs.all_world2pix(<span class="pl-c1">self</span>.radec.loc[<span class="pl-c1">1</span>:, <span class="pl-s"><span class="pl-pds">&#39;</span>RA<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">self</span>.radec.loc[<span class="pl-c1">1</span>:, <span class="pl-s"><span class="pl-pds">&#39;</span>DEC<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L1414" class="blob-num js-line-number" data-line-number="1414"></td>
        <td id="LC1414" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1415" class="blob-num js-line-number" data-line-number="1415"></td>
        <td id="LC1415" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> plot (including interactive step if requested)</span></td>
      </tr>
      <tr>
        <td id="L1416" class="blob-num js-line-number" data-line-number="1416"></td>
        <td id="LC1416" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> ax <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1417" class="blob-num js-line-number" data-line-number="1417"></td>
        <td id="LC1417" class="blob-code blob-code-inner js-file-line">            fig, ax <span class="pl-k">=</span> plt.subplots(<span class="pl-v">figsize</span> <span class="pl-k">=</span> (<span class="pl-c1">8</span>, <span class="pl-c1">8</span>))</td>
      </tr>
      <tr>
        <td id="L1418" class="blob-num js-line-number" data-line-number="1418"></td>
        <td id="LC1418" class="blob-code blob-code-inner js-file-line">        z <span class="pl-k">=</span> ZScaleInterval()</td>
      </tr>
      <tr>
        <td id="L1419" class="blob-num js-line-number" data-line-number="1419"></td>
        <td id="LC1419" class="blob-code blob-code-inner js-file-line">        zlim <span class="pl-k">=</span> z.get_limits(im.data)</td>
      </tr>
      <tr>
        <td id="L1420" class="blob-num js-line-number" data-line-number="1420"></td>
        <td id="LC1420" class="blob-code blob-code-inner js-file-line">        ax.imshow(<span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">*</span>im, <span class="pl-v">cmap</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>gray<span class="pl-pds">&#39;</span></span>, <span class="pl-v">vmin</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">*</span>zlim[<span class="pl-c1">1</span>], <span class="pl-v">vmax</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">*</span>zlim[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1421" class="blob-num js-line-number" data-line-number="1421"></td>
        <td id="LC1421" class="blob-code blob-code-inner js-file-line">        ax.plot(sn_x, sn_y, <span class="pl-s"><span class="pl-pds">&#39;</span>mD<span class="pl-pds">&#39;</span></span>, <span class="pl-v">markersize</span> <span class="pl-k">=</span> <span class="pl-c1">15</span>, <span class="pl-v">mfc</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>none<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mew</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1422" class="blob-num js-line-number" data-line-number="1422"></td>
        <td id="LC1422" class="blob-code blob-code-inner js-file-line">        ax.plot(rd_x, rd_y, <span class="pl-s"><span class="pl-pds">&#39;</span>bs<span class="pl-pds">&#39;</span></span>, <span class="pl-v">markersize</span> <span class="pl-k">=</span> <span class="pl-c1">15</span>, <span class="pl-v">mfc</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>none<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mew</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1423" class="blob-num js-line-number" data-line-number="1423"></td>
        <td id="LC1423" class="blob-code blob-code-inner js-file-line">        refp, <span class="pl-k">=</span> ax.plot(ref[<span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>], ref[<span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>ro<span class="pl-pds">&#39;</span></span>, <span class="pl-v">markersize</span> <span class="pl-k">=</span> <span class="pl-c1">15</span>, <span class="pl-v">mfc</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>none<span class="pl-pds">&#39;</span></span>, <span class="pl-v">picker</span> <span class="pl-k">=</span> <span class="pl-c1">14</span>, <span class="pl-v">mew</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1424" class="blob-num js-line-number" data-line-number="1424"></td>
        <td id="LC1424" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> idx, row <span class="pl-k">in</span> ref.iterrows():</td>
      </tr>
      <tr>
        <td id="L1425" class="blob-num js-line-number" data-line-number="1425"></td>
        <td id="LC1425" class="blob-code blob-code-inner js-file-line">            ax.annotate(idx, (row[<span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> <span class="pl-c1">20</span><span class="pl-k">*</span>head[<span class="pl-s"><span class="pl-pds">&#39;</span>NAXIS1<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span><span class="pl-c1">1024</span>, row[<span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>]), <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>, <span class="pl-v">size</span> <span class="pl-k">=</span> <span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L1426" class="blob-num js-line-number" data-line-number="1426"></td>
        <td id="LC1426" class="blob-code blob-code-inner js-file-line">        ax.set_xticks(())</td>
      </tr>
      <tr>
        <td id="L1427" class="blob-num js-line-number" data-line-number="1427"></td>
        <td id="LC1427" class="blob-code blob-code-inner js-file-line">        ax.set_yticks(())</td>
      </tr>
      <tr>
        <td id="L1428" class="blob-num js-line-number" data-line-number="1428"></td>
        <td id="LC1428" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> icut <span class="pl-k">==</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1429" class="blob-num js-line-number" data-line-number="1429"></td>
        <td id="LC1429" class="blob-code blob-code-inner js-file-line">            cut_list <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1430" class="blob-num js-line-number" data-line-number="1430"></td>
        <td id="LC1430" class="blob-code blob-code-inner js-file-line">            plt.ion()</td>
      </tr>
      <tr>
        <td id="L1431" class="blob-num js-line-number" data-line-number="1431"></td>
        <td id="LC1431" class="blob-code blob-code-inner js-file-line">            cid <span class="pl-k">=</span> fig.canvas.mpl_connect(<span class="pl-s"><span class="pl-pds">&#39;</span>pick_event<span class="pl-pds">&#39;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span>: onpick(event, cut_list, ref, refp, fig))</td>
      </tr>
      <tr>
        <td id="L1432" class="blob-num js-line-number" data-line-number="1432"></td>
        <td id="LC1432" class="blob-code blob-code-inner js-file-line">            fig.show()</td>
      </tr>
      <tr>
        <td id="L1433" class="blob-num js-line-number" data-line-number="1433"></td>
        <td id="LC1433" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>click on circled reference stars to be removed [hit &quot;enter&quot; when done]<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1434" class="blob-num js-line-number" data-line-number="1434"></td>
        <td id="LC1434" class="blob-code blob-code-inner js-file-line">            fig.canvas.mpl_disconnect(cid)</td>
      </tr>
      <tr>
        <td id="L1435" class="blob-num js-line-number" data-line-number="1435"></td>
        <td id="LC1435" class="blob-code blob-code-inner js-file-line">            plt.ioff()</td>
      </tr>
      <tr>
        <td id="L1436" class="blob-num js-line-number" data-line-number="1436"></td>
        <td id="LC1436" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.cal_IDs <span class="pl-k">=</span> <span class="pl-c1">self</span>.cal_IDs.drop(cut_list)</td>
      </tr>
      <tr>
        <td id="L1437" class="blob-num js-line-number" data-line-number="1437"></td>
        <td id="LC1437" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> display <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1438" class="blob-num js-line-number" data-line-number="1438"></td>
        <td id="LC1438" class="blob-code blob-code-inner js-file-line">            plt.ion()</td>
      </tr>
      <tr>
        <td id="L1439" class="blob-num js-line-number" data-line-number="1439"></td>
        <td id="LC1439" class="blob-code blob-code-inner js-file-line">            plt.show()</td>
      </tr>
      <tr>
        <td id="L1440" class="blob-num js-line-number" data-line-number="1440"></td>
        <td id="LC1440" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1441" class="blob-num js-line-number" data-line-number="1441"></td>
        <td id="LC1441" class="blob-code blob-code-inner js-file-line">            plt.savefig(os.path.join(<span class="pl-c1">self</span>.calibration_dir, <span class="pl-s"><span class="pl-pds">&#39;</span>ref_stars.png<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1442" class="blob-num js-line-number" data-line-number="1442"></td>
        <td id="LC1442" class="blob-code blob-code-inner js-file-line">            plt.close()</td>
      </tr>
      <tr>
        <td id="L1443" class="blob-num js-line-number" data-line-number="1443"></td>
        <td id="LC1443" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1444" class="blob-num js-line-number" data-line-number="1444"></td>
        <td id="LC1444" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">compare_image2ref</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">idx</span>):</td>
      </tr>
      <tr>
        <td id="L1445" class="blob-num js-line-number" data-line-number="1445"></td>
        <td id="LC1445" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>plot ref image and selected image side by side<span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1446" class="blob-num js-line-number" data-line-number="1446"></td>
        <td id="LC1446" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1447" class="blob-num js-line-number" data-line-number="1447"></td>
        <td id="LC1447" class="blob-code blob-code-inner js-file-line">        fig <span class="pl-k">=</span> plt.figure(<span class="pl-v">figsize</span> <span class="pl-k">=</span> (<span class="pl-c1">12</span>, <span class="pl-c1">6</span>))</td>
      </tr>
      <tr>
        <td id="L1448" class="blob-num js-line-number" data-line-number="1448"></td>
        <td id="LC1448" class="blob-code blob-code-inner js-file-line">        ref <span class="pl-k">=</span> Phot(<span class="pl-c1">self</span>.refname)</td>
      </tr>
      <tr>
        <td id="L1449" class="blob-num js-line-number" data-line-number="1449"></td>
        <td id="LC1449" class="blob-code blob-code-inner js-file-line">        wcs1 <span class="pl-k">=</span> WCS(<span class="pl-v">header</span> <span class="pl-k">=</span> ref.header)</td>
      </tr>
      <tr>
        <td id="L1450" class="blob-num js-line-number" data-line-number="1450"></td>
        <td id="LC1450" class="blob-code blob-code-inner js-file-line">        ax1 <span class="pl-k">=</span> fig.add_subplot(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">1</span>, <span class="pl-v">projection</span> <span class="pl-k">=</span> wcs1)</td>
      </tr>
      <tr>
        <td id="L1451" class="blob-num js-line-number" data-line-number="1451"></td>
        <td id="LC1451" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._display_refstars(<span class="pl-v">ax</span> <span class="pl-k">=</span> ax1)</td>
      </tr>
      <tr>
        <td id="L1452" class="blob-num js-line-number" data-line-number="1452"></td>
        <td id="LC1452" class="blob-code blob-code-inner js-file-line">        wcs2 <span class="pl-k">=</span> WCS(<span class="pl-v">header</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.phot_instances.loc[idx].header)</td>
      </tr>
      <tr>
        <td id="L1453" class="blob-num js-line-number" data-line-number="1453"></td>
        <td id="LC1453" class="blob-code blob-code-inner js-file-line">        ax2 <span class="pl-k">=</span> fig.add_subplot(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">2</span>, <span class="pl-v">projection</span> <span class="pl-k">=</span> wcs2)</td>
      </tr>
      <tr>
        <td id="L1454" class="blob-num js-line-number" data-line-number="1454"></td>
        <td id="LC1454" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phot_instances.loc[idx].display_image(<span class="pl-v">ax</span> <span class="pl-k">=</span> ax2, <span class="pl-v">display</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1455" class="blob-num js-line-number" data-line-number="1455"></td>
        <td id="LC1455" class="blob-code blob-code-inner js-file-line">        fig.show()</td>
      </tr>
      <tr>
        <td id="L1456" class="blob-num js-line-number" data-line-number="1456"></td>
        <td id="LC1456" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1457" class="blob-num js-line-number" data-line-number="1457"></td>
        <td id="LC1457" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> provide script functionality via</span></td>
      </tr>
      <tr>
        <td id="L1458" class="blob-num js-line-number" data-line-number="1458"></td>
        <td id="LC1458" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> python LPP.py name</span></td>
      </tr>
      <tr>
        <td id="L1459" class="blob-num js-line-number" data-line-number="1459"></td>
        <td id="LC1459" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1460" class="blob-num js-line-number" data-line-number="1460"></td>
        <td id="LC1460" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> argparse</td>
      </tr>
      <tr>
        <td id="L1461" class="blob-num js-line-number" data-line-number="1461"></td>
        <td id="LC1461" class="blob-code blob-code-inner js-file-line">    parser <span class="pl-k">=</span> argparse.ArgumentParser()</td>
      </tr>
      <tr>
        <td id="L1462" class="blob-num js-line-number" data-line-number="1462"></td>
        <td id="LC1462" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>name of the object<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1463" class="blob-num js-line-number" data-line-number="1463"></td>
        <td id="LC1463" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-a<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--add-images(s)<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>new<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L1464" class="blob-num js-line-number" data-line-number="1464"></td>
        <td id="LC1464" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>new image(s) or photlist to process<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1465" class="blob-num js-line-number" data-line-number="1465"></td>
        <td id="LC1465" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-i<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--interactive<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>interactive<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>store_const<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1466" class="blob-num js-line-number" data-line-number="1466"></td>
        <td id="LC1466" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">const</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>run in interactive mode<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1467" class="blob-num js-line-number" data-line-number="1467"></td>
        <td id="LC1467" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-ct<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--force-color-term<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>force_color_term<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, </td>
      </tr>
      <tr>
        <td id="L1468" class="blob-num js-line-number" data-line-number="1468"></td>
        <td id="LC1468" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>force to use specified color term<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1469" class="blob-num js-line-number" data-line-number="1469"></td>
        <td id="LC1469" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-dd<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--disc-date-mjd<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>disc_date_mjd<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">float</span>,</td>
      </tr>
      <tr>
        <td id="L1470" class="blob-num js-line-number" data-line-number="1470"></td>
        <td id="LC1470" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mjd of discovery<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1471" class="blob-num js-line-number" data-line-number="1471"></td>
        <td id="LC1471" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-c<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--cut-lc-points<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>lc_file<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>,</td>
      </tr>
      <tr>
        <td id="L1472" class="blob-num js-line-number" data-line-number="1472"></td>
        <td id="LC1472" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>light curve file to cut points from<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1473" class="blob-num js-line-number" data-line-number="1473"></td>
        <td id="LC1473" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-cr<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--cut-raw-lc-points-and-regenerate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>raw_lc_file<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>,</td>
      </tr>
      <tr>
        <td id="L1474" class="blob-num js-line-number" data-line-number="1474"></td>
        <td id="LC1474" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>light curve file to cut points from<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1475" class="blob-num js-line-number" data-line-number="1475"></td>
        <td id="LC1475" class="blob-code blob-code-inner js-file-line">    args <span class="pl-k">=</span> parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L1476" class="blob-num js-line-number" data-line-number="1476"></td>
        <td id="LC1476" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1477" class="blob-num js-line-number" data-line-number="1477"></td>
        <td id="LC1477" class="blob-code blob-code-inner js-file-line">    pipeline <span class="pl-k">=</span> LPP(args.name, <span class="pl-v">interactive</span> <span class="pl-k">=</span> args.interactive, <span class="pl-v">force_color_term</span> <span class="pl-k">=</span> args.force_color_term)</td>
      </tr>
      <tr>
        <td id="L1478" class="blob-num js-line-number" data-line-number="1478"></td>
        <td id="LC1478" class="blob-code blob-code-inner js-file-line">    pipeline.disc_date_mjd <span class="pl-k">=</span> args.disc_date_mjd</td>
      </tr>
      <tr>
        <td id="L1479" class="blob-num js-line-number" data-line-number="1479"></td>
        <td id="LC1479" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> (args.new <span class="pl-k">is</span> <span class="pl-c1">False</span>) <span class="pl-k">and</span> (args.lc_file <span class="pl-k">is</span> <span class="pl-c1">None</span>) <span class="pl-k">and</span> (args.raw_lc_file <span class="pl-k">is</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1480" class="blob-num js-line-number" data-line-number="1480"></td>
        <td id="LC1480" class="blob-code blob-code-inner js-file-line">        pipeline.run()</td>
      </tr>
      <tr>
        <td id="L1481" class="blob-num js-line-number" data-line-number="1481"></td>
        <td id="LC1481" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> (args.new <span class="pl-k">is</span> <span class="pl-c1">False</span>) <span class="pl-k">and</span> (args.lc_file <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1482" class="blob-num js-line-number" data-line-number="1482"></td>
        <td id="LC1482" class="blob-code blob-code-inner js-file-line">        pipeline.cut_lc_points(args.lc_file)</td>
      </tr>
      <tr>
        <td id="L1483" class="blob-num js-line-number" data-line-number="1483"></td>
        <td id="LC1483" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> (args.new <span class="pl-k">is</span> <span class="pl-c1">False</span>) <span class="pl-k">and</span> (args.raw_lc_file <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1484" class="blob-num js-line-number" data-line-number="1484"></td>
        <td id="LC1484" class="blob-code blob-code-inner js-file-line">        pipeline.cut_lc_points(args.raw_lc_file, <span class="pl-v">regenerate</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1485" class="blob-num js-line-number" data-line-number="1485"></td>
        <td id="LC1485" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1486" class="blob-num js-line-number" data-line-number="1486"></td>
        <td id="LC1486" class="blob-code blob-code-inner js-file-line">        pipeline.load() <span class="pl-c"><span class="pl-c">#</span> load from sav file</span></td>
      </tr>
      <tr>
        <td id="L1487" class="blob-num js-line-number" data-line-number="1487"></td>
        <td id="LC1487" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_c.fit<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> args.new:</td>
      </tr>
      <tr>
        <td id="L1488" class="blob-num js-line-number" data-line-number="1488"></td>
        <td id="LC1488" class="blob-code blob-code-inner js-file-line">            new_images <span class="pl-k">=</span> [fl.strip() <span class="pl-k">for</span> fl <span class="pl-k">in</span> args.new.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L1489" class="blob-num js-line-number" data-line-number="1489"></td>
        <td id="LC1489" class="blob-code blob-code-inner js-file-line">            pipeline.process_new_images(<span class="pl-v">new_image_list</span> <span class="pl-k">=</span> new_images)</td>
      </tr>
      <tr>
        <td id="L1490" class="blob-num js-line-number" data-line-number="1490"></td>
        <td id="LC1490" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: <span class="pl-c"><span class="pl-c">#</span> otherwise it is a photlist</span></td>
      </tr>
      <tr>
        <td id="L1491" class="blob-num js-line-number" data-line-number="1491"></td>
        <td id="LC1491" class="blob-code blob-code-inner js-file-line">            pipeline.process_new_images(<span class="pl-v">new_image_file</span> <span class="pl-k">=</span> args.new)</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/benstahl92/LOSSPhotPypeline/blame/5a1154fb0792e32accf6ed2174746fdafdabc661/LOSSPhotPypeline/pipeline/LPP.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/benstahl92/LOSSPhotPypeline/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>
  

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2019 <span title="0.22158s from unicorn-6fdf548986-ghh96">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-47ZXWJASen/yLysPiEpAb7/WvHBIHIRKo+7W5g0YYFiInTWqpjYBHTpeHut0QWEf51gExNhSEy55XQmxrZ+0xA==" type="application/javascript" src="https://github.githubassets.com/assets/compat-742699bf681282d2e3cf809d2b9de73a.js"></script>
    <script crossorigin="anonymous" integrity="sha512-YfiOQfcBmPBSdKjr8AOICO9fwE7C3m6h7nTT1o9oWwVsonJudi++Oqyd2wCynfJ6pyTXVFsqsv0aNhc+KJOuFw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-482260f8755c70642a3ef1f1448e1c47.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-S0voSoJpq5GHYxOnoCJQ+O0atQxEhtUco3qnjePJDk3nVCtahz+dfUEylxi4nyJFRM3WdWxftSzrIYy4DTiWOw==" type="application/javascript" src="https://github.githubassets.com/assets/github-c5900c16c89db65155e30edf06647291.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

