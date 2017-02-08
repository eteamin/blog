import json

from aiohttp.web import HTTPOk, HTTPBadRequest
from aiohttp_mako import template

from blog.models.post import Post
from blog.helpers import authorize
from blog import wsgi


@template('index.mak')
async def root(request):
    result = wsgi.connection.get('test')
    return dict(ok=result)


@template('login.mak')
async def login(request):
    return dict(ok=True)


async def login_handler(request):
    params = await request.post()
    username = params.get('username')
    password = params.get('password')
    if username and password:
        result = json.loads(wsgi.connection.get('admin').decode())
        assert username == result['username']
        assert password == result['password']
        return HTTPOk()
    else:
        return HTTPBadRequest()


#
# @authorize
# @template('admin.mak')
# async def admin(request):
#     pass
#
#
