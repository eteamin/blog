# -*- coding: utf-8 -*-

import json
from os import path

from aiohttp.web import Application, run_app
from aiohttp_mako import setup as mako_setup, TemplateLookup
from aiohttp_session import setup
from aiohttp_session.redis_storage import RedisStorage
from aioredis import create_pool
import asyncio_redis

from aiohttp_session.redis_storage import RedisStorage

from blog.routes import routes

views_path = path.abspath(path.join(path.dirname(__file__), 'views'))
mako_tmp_path = path.abspath(path.join(path.dirname(__file__), 'mako_tmp'))
mako_lookup = TemplateLookup([views_path], module_directory=mako_tmp_path)
STATICS = path.abspath(path.join(path.dirname(__file__), 'public'))
configuration_file = path.abspath(path.join(path.dirname(__file__), 'configuration.json'))


def load_conf():
    with open(configuration_file, 'r') as c:
        return json.load(c)


def setup_mako_templates(app):
    # Setup Mako
    mako_engine = mako_setup(
        app,
        input_encoding='utf-8',
        output_encoding='utf-8',
        default_filters=['decode.utf8']
    )
    index_template = mako_lookup.get_template('index.mak')
    mako_engine.put_template('index.mak', index_template)

    admin_template = mako_lookup.get_template('admin.mak')
    mako_engine.put_template('admin.mak', admin_template)

    login_template = mako_lookup.get_template('login.mak')
    mako_engine.put_template('login.mak', login_template)


async def init_session(app):
    config = app['config']
    redis_host = config.get('redisHost')
    redis_port = config.get('redisPort')
    redis_db = config.get('redisDB')

    pool = await create_pool((redis_host, redis_port), db=redis_db)
    setup(app, RedisStorage(pool))


async def init_db_session(app):
    # Setup Session
    config = app['config']
    redis_host = config.get('redisHost')
    redis_port = config.get('redisPort')
    redis_db = config.get('redisDB')
    app['redis'] = await asyncio_redis.Connection.create(host=redis_host, port=redis_port, db=redis_db)


def make_app():
    blog = Application()
    blog['config'] = load_conf()

    # Assign Routes
    for r in routes():
        blog.router.add_route(r.method, r.path, r.handler)

    # Serve statics for development purposes
    blog.router.add_static('/css', path.join(STATICS, 'css'))
    blog.router.add_static('/js', path.join(STATICS, 'js'))
    blog.router.add_static('/images', path.join(STATICS, 'images'))
    blog.router.add_static('/storage', path.join(STATICS, 'storage'))

    # Setup Mako
    setup_mako_templates(blog)

    # Setup Session
    blog.on_startup.append(init_db_session)
    blog.on_startup.append(init_session)

    return blog


if __name__ == '__main__':
    run_app(make_app(), port=8585)

