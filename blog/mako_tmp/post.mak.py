# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1504978476.255356
_enable_loop = True
_template_filename = '/Users/etemin/workspace/blog/blog/views/post.mak'
_template_uri = 'post.mak'
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
        post = context.get('post', UNDEFINED)
        base_url = context.get('base_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')

        from datetime import datetime
        def string_to_datetime(s):
            return datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime','string_to_datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!-- .site-main -->\n<div id="main" class="site-main"> <!-- .blog-single -->\n  <div class="blog-single page-layout">\n\n\n      <!-- .layout-fixed -->\n      <div class="layout-fixed">\n\n\n\n          <!-- .hentry -->\n          <article class="post type-post hentry">\n\n\n              <!-- .entry-header -->\n              <header class="entry-header">\n                <h1 class="entry-title">')
        __M_writer(str(post.get('title')))
        __M_writer('</h1>\n\n                <!-- .entry-meta -->\n                <div class="entry-meta">\n                    <span class="entry-date">\n                        <time class="entry-date" datetime="2014-07-13T04:34:10+00:00"></time>\n                    </span>\n                    <!--<span class="edit-link">\n                        <a class="post-edit-link" href="#">Edit</a>\n                    </span>-->\n                </div>\n                <!-- .entry-meta -->\n\n              </header>\n              <!-- .entry-header -->\n\n              <!-- .featured-image -->\n              <div class="featured-image">\n                <img src="')
        __M_writer(str('{}/storage/{}'.format(base_url, post.get('title').replace(' ', '_'))))
        __M_writer('" alt="blog-image">\n              </div>\n              <!-- .featured-image -->\n\n\n              <!-- .entry-content -->\n              <div class="entry-content">\n\n                    ')
        __M_writer(post.get('description') )
        __M_writer('\n\n\n              </div>\n              <!-- .entry-content -->\n\n\n\n\n          </article>\n          <!-- .hentry -->\n\n\n\n          <!-- #comments -->\n\n\n\n      </div>\n      <!-- .layout-fixed -->\n\n\n  </div>\n  <!-- .blog-single -->\n\n\n\n</div>\n<!-- .site-main -->\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/etemin/workspace/blog/blog/views/post.mak", "uri": "post.mak", "line_map": {"48": 49, "43": 6, "34": 1, "35": 2, "49": 49, "55": 49, "27": 0, "44": 23, "45": 23, "46": 41, "47": 41}}
__M_END_METADATA
"""
