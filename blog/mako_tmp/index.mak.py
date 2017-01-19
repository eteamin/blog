# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484849894.6733642
_enable_loop = True
_template_filename = '/home/amin/workspace/web/blog/blog/views/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ok = context.get('ok', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(ok))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "28": 22, "22": 1}, "filename": "/home/amin/workspace/web/blog/blog/views/index.mak", "uri": "index.mak", "source_encoding": "ascii"}
__M_END_METADATA
"""
