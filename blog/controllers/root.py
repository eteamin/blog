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
    return dict(posts=posts, base_url=request.app['config'].get('base_url'))


@template('post.mak')
async def single(request):
    title = request.rel_url.name
    post = await request.app['redis'].get(title)
    return dict(post=json.loads(post), base_url=request.app['config'].get('base_url'))


@template('login.mak')
async def login(request):
    return dict()


async def login_handler(request):
    params = await request.post()
    username = params.get('username')
    password = params.get('password')
    session = await get_session(request)
    if username and password:
        admin = request.app['config'].get('admin')
        admin_passwod = request.app['config'].get('password')
        if username == admin and password == admin_passwod:
            session['allowed'] = True
            return HTTPFound('/admin')
        else:
            raise HTTPUnauthorized()
    else:
        raise HTTPBadRequest()


@template('admin.mak')
async def admin(request):
    session = await get_session(request)
    if not session.get('allowed'):
        raise HTTPUnauthorized()
    return dict()


async def submit_post(request):
    session = await get_session(request)
    if not session.get('allowed'):
        return HTTPUnauthorized()
    params = await request.post()
    title = params.get('title')
    description = params.get('description')
    image = params.get('image')
    if not title or not description:
        raise HTTPBadRequest()
    post = Post(title, description, image)
    if await request.app['redis'].get(post.title):
        raise HTTPBadRequest(text='Duplicate Title!')
    await post.store_image()
    await request.app['redis'].set(title.replace(' ', '-'), post.as_string())
    return HTTPFound('/')

