# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1504977973.80802
_enable_loop = True
_template_filename = '/Users/etemin/workspace/blog/blog/views/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'master.mak', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        base_url = context.get('base_url', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')

        from datetime import datetime
        def string_to_datetime(s):
            return datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['string_to_datetime','datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n            <!-- .site-main -->\n\t\t  <div id="main" class="site-main"> <!-- PAGE : HOME -->\n              <section id="home" class="pt-page page-layout light-text home-section has-bg-img" style="background-image:url(images/site/home.jpg)">\n               \t  <!-- .content -->\n                  <div class="content">\n                   \t  <!-- .layout-medium -->\n                      <div class="layout-medium">\n\n                          <h4>Hi</h4>\n                          <h2>I\'m Amin</h2>\n   \t\t\t\t\t  </div>\n                      <!-- .layout-medium -->\n                  </div>\n                  <!-- .content -->\n              </section>\n              <!-- PAGE : HOME -->\n\n\n              <!-- PAGE : ABOUT -->\n              <section id="about" class="pt-page page-layout">\n               \t  <!-- .content -->\n                  <div class="content">\n                   \t  <!-- .layout-medium -->\n                      <div class="layout-medium">\n\n\n                          <!-- page-title -->\n                          <h1 class="page-title">\n                              <i class="pe-7s-user"></i>About Me\n                          </h1>\n                          <!-- page-title -->\n\n\n\n\n                          <!-- SERVICES -->\n\n                          <!-- section-title -->\n                          <div class="section-title center">\n                              <h2>\n                                  <i>Skills</i>\n                              </h2>\n                          </div>\n                          <!-- section-title -->\n\n                          <!-- row -->\n                          <div class="row">\n\n                              <!-- col -->\n                              <div class="col-sm-6 col-md-3">\n\n                                  <!-- service -->\n                                  <div class="service">\n                                      <!--<i class="pe-7s-glasses"></i>-->\n                                      <img src="images/site/icon-01.png" alt="image"/>\n                                      <h4>Real-Time Translation</h4>\n                                      <p>I enjoy spending time as a real-time translator (Eng to Fa, Fa to Eng) from time to time.</p>\n                                  </div>\n                                  <!-- service -->\n\n                              </div>\n                              <!-- col -->\n\n                              <!-- col -->\n                              <div class="col-sm-6 col-md-3">\n\n                                  <!-- service -->\n                                  <div class="service">\n                                      <!--<i class="pe-7s-scissors"></i>-->\n                                      <img src="images/site/icon-04.png" alt="image"/>\n                                      <h4>Software Analyser</h4>\n                                      <p>I can give you advice on the tools to use and the attitude to grasp on the way of developing your software</p>\n                                  </div>\n                                  <!-- service -->\n\n                              </div>\n                              <!-- col -->\n\n                              <!-- col -->\n                              <div class="col-sm-6 col-md-3">\n\n                                  <!-- service -->\n                                  <div class="service">\n                                      <!--<i class="pe-7s-rocket"></i>-->\n                                      <img src="images/site/icon-03.png" alt="image"/>\n                                      <h4>Web Developer</h4>\n                                      <p>Full-Stack web developer interested in development using <a href="http://turbogears.org/">TurboGears</a>, <a href="http://aiohttp.readthedocs.io/en/stable/">aiohttp</a> and the fun-to-use <a href="http://cherrypy.org/">Cherrypy</a>.</p>\n                                  </div>\n                                  <!-- service -->\n\n                              </div>\n                              <!-- col -->\n                              <div class="col-sm-6 col-md-3">\n\n                                  <!-- service -->\n                                  <div class="service">\n                                      <!--<i class="pe-7s-joy"></i>-->\n                                      <img src="images/site/icon-02.png" alt="image"/>\n                                      <h4>Programmer</h4>\n                                      <p>I\'m a <a href="https://www.python.org/">Python</a> enthusiast, interested in GUI programming and also web programming with special regards to <a href="https://en.wikipedia.org/wiki/Test-driven_development">Test Driven Development</a>.</p>\n                                  </div>\n                                  <!-- service -->\n\n                              </div>\n                              <!-- col -->\n\n\n                                                              <!-- col -->\n\n                          </div>\n                          <!-- row -->\n                          <!-- SERVICES -->\n\n   \t\t\t\t\t  </div>\n                      <!-- .layout-medium -->\n                  </div>\n                  <!-- .content -->\n              </section>\n              <!-- PAGE : ABOUT -->\n\n\n\n              <!-- PAGE : BLOG -->\n              <section id="blog" class="pt-page page-layout">\n               \t  <!-- .content -->\n                  <div class="content">\n                   \t  <!-- .layout-medium -->\n                      <div class="layout-medium">\n\n\n                        <!-- page-title -->\n                        <h1 class="page-title">\n                        \t<i class="pe-7s-notebook"></i>Blog\n                        </h1>\n                        <!-- page-title -->\n\n\n                        <!--<div class="entry-content">\n                        \t<p>You don\'t know how to do any of those. What are their names? I\'ve been there. My folks were always on me to groom myself and wear underpants.</p>\n                        </div>-->\n\n\n                        <!-- LATEST POSTS -->\n                        <div class="latest-posts media-grid masonry" data-layout="masonry" data-item-width="340">\n\n')
        for p in posts:
            __M_writer('\n                                <!-- post -->\n                                <article class="hentry media-cell">\n\n                                    <div class="media-box">\n                                        <img src="')
            __M_writer(str('{}/storage/{}'.format(base_url, p.get('title').replace(' ', '_'))))
            __M_writer('" alt="post-image">\n                                        <div class="mask"></div>\n                                        <a href="')
            __M_writer(str('{}/posts/{}'.format(base_url, p.get('title').replace(' ', '-'))))
            __M_writer('"></a>\n                                    </div>\n\n                                    <header class="media-cell-desc">\n                                        <span title="2013" class="date">\n                                            <span class="day">')
            __M_writer(str(string_to_datetime(p.get('created')).day))
            __M_writer('</span>')
            __M_writer(str(string_to_datetime(p.get('created')).strftime('%B')))
            __M_writer('</span>\n                                        <h3>\n                                            <a href="')
            __M_writer(str('{}/posts/{}'.format(base_url, p.get('title').replace(' ', '-'))))
            __M_writer('">')
            __M_writer(str(p.get('title')))
            __M_writer('</a>\n                                        </h3>\n                                    </header>\n\n                                </article>\n                                <!-- post -->\n')
        __M_writer('\n\n                        </div>\n                        <!-- LATEST POSTS -->\n\n\n                        <p class="launch">\n                            <a class="button" href="blog.html">View All Posts</a>\n                        </p>\n\n\n   \t\t\t\t\t  </div>\n                      <!-- .layout-medium -->\n                  </div>\n                  <!-- .content -->\n              </section>\n              <!-- PAGE : BLOG -->\n\n\n              <!-- PAGE : CONTACT -->\n              <section id="contact" class="pt-page page-layout contact light-text">\n               \t  <!-- .content -->\n                  <div class="content">\n                   \t  <!-- .layout-medium -->\n                      <div class="layout-medium">\n\n\n                          <!-- page-title -->\n                          <h1 class="page-title">\n                              <i class="pe-7s-call"></i>Contact Me\n                          </h1>\n                          <!-- page-title -->\n\n\n\n\n                          <!-- section-title -->\n                          <div class="section-title center">\n                              <h2>\n                                  <i>Social Medias</i>\n                              </h2>\n                          </div>\n                          <!-- section-title -->\n\n                          <!-- SOCIAL -->\n                          <ul class="social">\n                              <li><a target="_blank"  href="https://t.me/eteamin"><img src="images/site/telegram.png"></a></li>\n                              <li><a target="_blank"  href="https://stackoverflow.com/users/6764079/juggernaut"><img src="images/site/stackoverflow.png"></a></li>\n                              <li><a target="_blank"  href="https://github.com/eteamin"><img src="images/site/github.png"></a></li>\n                          </ul>\n                            <!-- SOCIAL -->\n\n\n\n                          <!-- GOOGLE MAP -->\n                          <div class="map">\n                              <div data-latitude="35.820326" data-longitude="51.625485" data-zoom="5" data-marker-image="images/site/marker.png" id="map-canvas" class="map-canvas"></div>\n                          </div>\n                          <!-- GOOGLE MAP -->\n\n\n   \t\t\t\t\t  </div>\n                      <!-- .layout-medium -->\n                  </div>\n                  <!-- .content -->\n              </section>\n              <!-- PAGE : CONTACT -->\n\n\n\n        </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/etemin/workspace/blog/blog/views/index.mak", "source_encoding": "utf-8", "line_map": {"64": 58, "34": 1, "35": 2, "43": 6, "44": 152, "45": 153, "46": 158, "47": 158, "48": 160, "49": 160, "50": 165, "51": 165, "52": 165, "53": 165, "54": 167, "55": 167, "56": 167, "57": 167, "58": 174, "27": 0}, "uri": "index.mak"}
__M_END_METADATA
"""
