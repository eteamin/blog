import json

from aiohttp.web import HTTPOk, HTTPBadRequest
from aiohttp_mako import template
from aiohttp_session import get_session

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
    username = await params.get('username')
    password = await params.get('password')
    session = await get_session(request)
    if 'token' in session and session['token'] == token_secret
    if username and password:
        result = json.loads(wsgi.connection.get('admin').decode())
        if username == result['username'] and  password == result['password']:

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
