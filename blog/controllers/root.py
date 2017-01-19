import asyncio_redis
from aiohttp_mako import template

from blog.models.post import Post
from blog.helpers import authorize


@template('index.mak')
async def root(request):
    r = await asyncio_redis.Connection.create()
    # Getting the last 10 posts
    result = await r.get('test')
    return dict(ok=result)


@template('login.mak')
async def login(request):
    return dict(ok=True)


async def login_handler(request):
    pass

#
# @authorize
# @template('admin.mak')
# async def admin(request):
#     pass
#
#
