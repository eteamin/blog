<%inherit file="master.mak"/>
<%
    from datetime import datetime
    def string_to_datetime(s):
        return datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
%>
<!-- .site-main -->
<div id="main" class="site-main"> <!-- .blog-single -->
  <div class="blog-single page-layout">


      <!-- .layout-fixed -->
      <div class="layout-fixed">



          <!-- .hentry -->
          <article class="post type-post hentry">


              <!-- .entry-header -->
              <header class="entry-header">
                <h1 class="entry-title">${post.get('title')}</h1>

                <!-- .entry-meta -->
                <div class="entry-meta">
                    <span class="entry-date">
                        <time class="entry-date" datetime="2014-07-13T04:34:10+00:00"></time>
                    </span>
                    <!--<span class="edit-link">
                        <a class="post-edit-link" href="#">Edit</a>
                    </span>-->
                </div>
                <!-- .entry-meta -->

              </header>
              <!-- .entry-header -->

              <!-- .featured-image -->
              <div class="featured-image">
                <img src="${'{}/storage/{}'.format(base_url, post.get('title').replace(' ', '_'))}" alt="blog-image">
              </div>
              <!-- .featured-image -->


              <!-- .entry-content -->
              <div class="entry-content">

                    ${post.get('description') | n}


              </div>
              <!-- .entry-content -->




          </article>
          <!-- .hentry -->



          <!-- #comments -->



      </div>
      <!-- .layout-fixed -->


  </div>
  <!-- .blog-single -->



</div>
<!-- .site-main -->




