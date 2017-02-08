# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486510720.368556
_enable_loop = True
_template_filename = '/home/amin/workspace/web/blog/blog/views/login.mak'
_template_uri = 'login.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<form action="/login_handler" method="post">\n    <input type="text" name="username">\n    <input type="password" name="password">\n    <button type="submit">Login</button>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/home/amin/workspace/web/blog/blog/views/login.mak", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "login.mak"}
__M_END_METADATA
"""
