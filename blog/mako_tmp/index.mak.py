# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487292044.547348
_enable_loop = True
_template_filename = '/home/amin/workspace/web/blog/blog/views/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        result = context.get('result', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(result))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/amin/workspace/web/blog/blog/views/index.mak", "source_encoding": "ascii", "uri": "index.mak", "line_map": {"16": 0, "28": 22, "22": 1}}
__M_END_METADATA
"""
