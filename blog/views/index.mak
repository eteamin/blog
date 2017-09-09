<%inherit file="master.mak"/>
<%
    from datetime import datetime
    def string_to_datetime(s):
        return datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
%>
            <!-- .site-main -->
		  <div id="main" class="site-main"> <!-- PAGE : HOME -->
              <section id="home" class="pt-page page-layout light-text home-section has-bg-img" style="background-image:url(images/site/home.jpg)">
               	  <!-- .content -->
                  <div class="content">
                   	  <!-- .layout-medium -->
                      <div class="layout-medium">

                          <h4>Hi</h4>
                          <h2>I'm Amin</h2>
   					  </div>
                      <!-- .layout-medium -->
                  </div>
                  <!-- .content -->
              </section>
              <!-- PAGE : HOME -->


              <!-- PAGE : ABOUT -->
              <section id="about" class="pt-page page-layout">
               	  <!-- .content -->
                  <div class="content">
                   	  <!-- .layout-medium -->
                      <div class="layout-medium">


                          <!-- page-title -->
                          <h1 class="page-title">
                              <i class="pe-7s-user"></i>About Me
                          </h1>
                          <!-- page-title -->




                          <!-- SERVICES -->

                          <!-- section-title -->
                          <div class="section-title center">
                              <h2>
                                  <i>Skills</i>
                              </h2>
                          </div>
                          <!-- section-title -->

                          <!-- row -->
                          <div class="row">

                              <!-- col -->
                              <div class="col-sm-6 col-md-3">

                                  <!-- service -->
                                  <div class="service">
                                      <!--<i class="pe-7s-glasses"></i>-->
                                      <img src="images/site/icon-01.png" alt="image"/>
                                      <h4>Real-Time Translation</h4>
                                      <p>I enjoy spending time as a real-time translator (Eng to Fa, Fa to Eng) from time to time.</p>
                                  </div>
                                  <!-- service -->

                              </div>
                              <!-- col -->

                              <!-- col -->
                              <div class="col-sm-6 col-md-3">

                                  <!-- service -->
                                  <div class="service">
                                      <!--<i class="pe-7s-scissors"></i>-->
                                      <img src="images/site/icon-04.png" alt="image"/>
                                      <h4>Software Analyser</h4>
                                      <p>I can give you advice on the tools to use and the attitude to grasp on the way of developing your software</p>
                                  </div>
                                  <!-- service -->

                              </div>
                              <!-- col -->

                              <!-- col -->
                              <div class="col-sm-6 col-md-3">

                                  <!-- service -->
                                  <div class="service">
                                      <!--<i class="pe-7s-rocket"></i>-->
                                      <img src="images/site/icon-03.png" alt="image"/>
                                      <h4>Web Developer</h4>
                                      <p>Full-Stack web developer interested in development using <a href="http://turbogears.org/">TurboGears</a>, <a href="http://aiohttp.readthedocs.io/en/stable/">aiohttp</a> and the fun-to-use <a href="http://cherrypy.org/">Cherrypy</a>.</p>
                                  </div>
                                  <!-- service -->

                              </div>
                              <!-- col -->
                              <div class="col-sm-6 col-md-3">

                                  <!-- service -->
                                  <div class="service">
                                      <!--<i class="pe-7s-joy"></i>-->
                                      <img src="images/site/icon-02.png" alt="image"/>
                                      <h4>Programmer</h4>
                                      <p>I'm a <a href="https://www.python.org/">Python</a> enthusiast, interested in GUI programming and also web programming with special regards to <a href="https://en.wikipedia.org/wiki/Test-driven_development">Test Driven Development</a>.</p>
                                  </div>
                                  <!-- service -->

                              </div>
                              <!-- col -->


                                                              <!-- col -->

                          </div>
                          <!-- row -->
                          <!-- SERVICES -->

   					  </div>
                      <!-- .layout-medium -->
                  </div>
                  <!-- .content -->
              </section>
              <!-- PAGE : ABOUT -->



              <!-- PAGE : BLOG -->
              <section id="blog" class="pt-page page-layout">
               	  <!-- .content -->
                  <div class="content">
                   	  <!-- .layout-medium -->
                      <div class="layout-medium">


                        <!-- page-title -->
                        <h1 class="page-title">
                        	<i class="pe-7s-notebook"></i>Blog
                        </h1>
                        <!-- page-title -->


                        <!--<div class="entry-content">
                        	<p>You don't know how to do any of those. What are their names? I've been there. My folks were always on me to groom myself and wear underpants.</p>
                        </div>-->


                        <!-- LATEST POSTS -->
                        <div class="latest-posts media-grid masonry" data-layout="masonry" data-item-width="340">

                            %for p in posts:

                                <!-- post -->
                                <article class="hentry media-cell">

                                    <div class="media-box">
                                        <img src="${'{}/storage/{}'.format(base_url, p.get('title').replace(' ', '_'))}" alt="post-image">
                                        <div class="mask"></div>
                                        <a href="${'{}/posts/{}'.format(base_url, p.get('title').replace(' ', '-'))}"></a>
                                    </div>

                                    <header class="media-cell-desc">
                                        <span title="2013" class="date">
                                            <span class="day">${string_to_datetime(p.get('created')).day}</span>${string_to_datetime(p.get('created')).strftime('%B')}</span>
                                        <h3>
                                            <a href="${'{}/posts/{}'.format(base_url, p.get('title').replace(' ', '-'))}">${p.get('title')}</a>
                                        </h3>
                                    </header>

                                </article>
                                <!-- post -->
                            %endfor


                        </div>
                        <!-- LATEST POSTS -->


                        <p class="launch">
                            <a class="button" href="blog.html">View All Posts</a>
                        </p>


   					  </div>
                      <!-- .layout-medium -->
                  </div>
                  <!-- .content -->
              </section>
              <!-- PAGE : BLOG -->


              <!-- PAGE : CONTACT -->
              <section id="contact" class="pt-page page-layout contact light-text">
               	  <!-- .content -->
                  <div class="content">
                   	  <!-- .layout-medium -->
                      <div class="layout-medium">


                          <!-- page-title -->
                          <h1 class="page-title">
                              <i class="pe-7s-call"></i>Contact Me
                          </h1>
                          <!-- page-title -->




                          <!-- section-title -->
                          <div class="section-title center">
                              <h2>
                                  <i>Social Medias</i>
                              </h2>
                          </div>
                          <!-- section-title -->

                          <!-- SOCIAL -->
                          <ul class="social">
                              <li><a target="_blank"  href="https://t.me/eteamin"><img src="images/site/telegram.png"></a></li>
                              <li><a target="_blank"  href="https://stackoverflow.com/users/6764079/juggernaut"><img src="images/site/stackoverflow.png"></a></li>
                              <li><a target="_blank"  href="https://github.com/eteamin"><img src="images/site/github.png"></a></li>
                          </ul>
                            <!-- SOCIAL -->



                          <!-- GOOGLE MAP -->
                          <div class="map">
                              <div data-latitude="35.820326" data-longitude="51.625485" data-zoom="5" data-marker-image="images/site/marker.png" id="map-canvas" class="map-canvas"></div>
                          </div>
                          <!-- GOOGLE MAP -->


   					  </div>
                      <!-- .layout-medium -->
                  </div>
                  <!-- .content -->
              </section>
              <!-- PAGE : CONTACT -->



        </div>