import json

from aiohttp.web import HTTPFound, HTTPUnauthorized, HTTPBadRequest
from aiohttp_mako import template
from aiohttp_session import get_session

from blog.models.post import Post


@template('index.mak')
async def index(request):
    posts = []
    all = await request.app['redis'].keys(pattern='*')
    for r in all:
        v = await request.app['redis'].get(r.result())
        posts.append(json.loads(v))
    return dict(posts=posts)


@template('login.mak')
async def login(request):
    return dict()


async def login_handler(request):
    params = await request.post()
    username = params.get('username')
    password = params.get('password')
    session = await get_session(request)
    # If already logged in
    if 'token' in session and session['token'] == request.app['config'].get('token'):
        return HTTPFound('/')
    if username and password:
        result = json.loads(request.app['config'].get('admin').decode())
        if username == result['username'] and password == result['password']:
            session['token'] = request.app['config'].get('token')
            return HTTPFound('/admin')
        else:
            return HTTPUnauthorized()
    else:
        return HTTPBadRequest()


@template('admin.mak')
# @authorize
async def admin(request):
    return dict()


# @authorize
async def submit_post(request):
    params = await request.post()
    title = params.get('title')
    description = params.get('description')
    image = params.get('image')
    if not title or not description:
        return HTTPBadRequest()
    post = Post(title, description, image)
    if await request.app['redis'].get(post.title):
        return HTTPBadRequest(text='Duplicate Title!')
    await post.store_image()
    await request.app['redis'].set(title, post.as_string())
    return HTTPFound('/')

