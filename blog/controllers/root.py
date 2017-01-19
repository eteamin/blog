from aiohttp_mako import template

from blog.helpers import authorize


@template('index.mak')
async def root(request):
    return dict(ok=True)


@template('login.mak')
async def login(request):
    return dict(ok=True)


async def login_handler(request):
    pass


@authorize
@template('admin.mak')
async def admin(request):
    pass


