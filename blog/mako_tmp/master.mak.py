# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1504979110.320596
_enable_loop = True
_template_filename = '/Users/etemin/workspace/blog/blog/views/master.mak'
_template_uri = 'master.mak'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        base_url = context.get('base_url', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en" class="no-js one-page-layout" data-mobile-classic-layout="false" data-classic-layout="false" data-prev-animation="16" data-next-animation="15" data-random-animation="false">\n    <head>\n\n        <meta charset="utf-8" />\n        <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">\n        <meta name="description" content="">\n        <meta name="keywords" content="Python, WebDeveloper">\n        <meta name="author" content="Amin Etesamian">\n\n        <title>Amin Etesamian - امین اعتصامیان</title>\n\n        <!-- FAV and TOUCH ICONS -->\n        <link rel="shortcut icon" href="')
        __M_writer(str('{}/images/ico/favicon.ico'.format(base_url)))
        __M_writer('">\n        <link rel="apple-touch-icon" href="images/ico/apple-touch-icon.png"/>\n\n        <!-- STYLES -->\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/bootstrap.min.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/bootstrap-rtl.min.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/fonts/pe-icon-7-stroke/css/pe-icon-7-stroke.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/fonts/fontello/css/fontello.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/js/nprogress/nprogress.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/js/jquery.magnific-popup/magnific-popup.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/animations.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/align1.0.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/main1.0.css'.format(base_url)))
        __M_writer('">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str('{}/css/7681.0.css'.format(base_url)))
        __M_writer('">\n\n        <!-- INITIAL SCRIPTS -->\n        <script src="')
        __M_writer(str('{}/js/jquery-1.12.1.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/jquery-migrate-1.2.1.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/modernizr.min.js'.format(base_url)))
        __M_writer('"></script>\n    <!--[if lt IE 9]>\n            <script src="')
        __M_writer(str('{}/js/ie.js'.format(base_url)))
        __M_writer('"></script>\n        <![endif]-->\n\n    </head>\n\n\n\n    <body>\n\n\n        <!-- PAGE -->\n\t<div id="page" class="hfeed site">\n\n            <!-- HEADER -->\n            <header id="masthead" class="header" role="banner">\n\n                <a class="menu-toggle toggle-link"></a>\n\n                <h1 class="site-title mobile-title">Amin Etesamian</h1>\n\n                <!-- header-wrap -->\n                <div class="header-wrap">\n\n                    <img src="')
        __M_writer(str('{}/images/site/avatar.jpg'.format(base_url)))
        __M_writer('" alt="avatar">\n\n                    <h1 class="site-title">Amin Etesamian</h1>\n\n                    <!-- NAV MENU -->\n                    <nav id="primary-navigation" class="site-navigation primary-navigation" role="navigation">\n                        <div class="nav-menu">\n                            <ul>\n\t\t\t\t\t\t\t<li>\n                            <a href="#/home">\n                                <i class="pe-7s-home"></i>Home</a>\n                            </li>\n                                <li>\n                                    <a href="#/about">\n                                        <i class="pe-7s-user"></i>About Me</a>\n                                </li>\n                                <li>\n                                    <a href="#/blog">\n                                        <i class="pe-7s-notebook"></i>Blog</a>\n                                </li>\n                                <li>\n                                    <a href="#/contact">\n                                        <i class="pe-7s-call"></i>Contact</a>\n                                </li>\n\n                            </ul>\n                        </div>\n                    </nav>\n                    <!-- NAV MENU -->\n\n\n\n                    <!-- SEARCH -->\n\n                    <!-- SEARCH -->\n\n                    <!-- header-bottom -->\n                    <div class="header-bottom">\n\n                        <!-- SOCIAL -->\n                        <ul class="social">\n                            <li>\n                                <a class="github" href="https://github.com/eteamin"></a>\n                            </li>\n\n                        </ul>\n                        <!-- SOCIAL -->\n\n                        <!-- copy-text -->\n                        <div class="copy-text">\n                        \t<p>&copy; Amin Etesamian 2017</p>\n                        </div>\n                        <!-- copy-text -->\n\n                    </div>\n                    <!-- header-bottom -->\n\n\n                </div>\n                <!-- header-wrap -->\n\n\t\t\t</header>\n            <!-- HEADER -->\n\n\n            ')
        __M_writer(str(next.body()))
        __M_writer('\n            <!-- .site-main -->\n\n\t\t</div>\n        <!-- PAGE -->\n\n\n   \t<!-- SCRIPTS -->\n        <script src="')
        __M_writer(str('{}/js/jquery.address-1.5.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/nprogress/nprogress.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/fastclick.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/typist.js'.format(base_url)))
        __M_writer('"></script>\n\t\t<script src="')
        __M_writer(str('{}/js/imagesloaded.pkgd.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/jquery.isotope.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/jquery.validate.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/jquery.magnific-popup/jquery.magnific-popup.min.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/socialstream.jquery.js'.format(base_url)))
        __M_writer('"></script>\n        <script src="')
        __M_writer(str('{}/js/main.js'.format(base_url)))
        __M_writer('"></script>\n        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "23": 1, "24": 16, "25": 16, "26": 20, "27": 20, "28": 21, "29": 21, "30": 22, "31": 22, "32": 23, "33": 23, "34": 24, "35": 24, "36": 25, "37": 25, "38": 26, "39": 26, "40": 27, "41": 27, "42": 28, "43": 28, "44": 29, "45": 29, "46": 32, "47": 32, "48": 33, "49": 33, "50": 34, "51": 34, "52": 36, "53": 36, "54": 59, "55": 59, "56": 124, "57": 124, "58": 132, "59": 132, "60": 133, "61": 133, "62": 134, "63": 134, "64": 135, "65": 135, "66": 136, "67": 136, "68": 137, "69": 137, "70": 138, "71": 138, "72": 139, "73": 139, "74": 140, "75": 140, "76": 141, "77": 141, "83": 77}, "uri": "master.mak", "source_encoding": "utf-8", "filename": "/Users/etemin/workspace/blog/blog/views/master.mak"}
__M_END_METADATA
"""
