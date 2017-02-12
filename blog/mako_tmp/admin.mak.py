# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486927783.9316592
_enable_loop = True
_template_filename = '/home/amin/workspace/web/blog/blog/views/admin.mak'
_template_uri = 'admin.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<form action="/admin/submit_post" method="post" enctype="multipart/form-data">\n    <input type="text" name="title">\n    <input type="text" name="description">\n    <input type="file" name="image">\n    <button type="submit">Submit</button>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "admin.mak", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii", "filename": "/home/amin/workspace/web/blog/blog/views/admin.mak"}
__M_END_METADATA
"""
