from os import path
import base64

from aiohttp_mako import TemplateLookup, setup as make_configuration
from aiohttp.web import Application, run_app

from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import redis

from blog import views, mako_tmp
from blog.controllers.root import root, login, login_handler

connection = redis.StrictRedis()


def make_app():
    # Routes
    app = Application()
    app.router.add_route('GET', '/', root)
    app.router.add_route('GET', '/login', login)
    app.router.add_route('POST', '/login_handler', login_handler)

    # Setup and configure Mako
    mako_setup = make_configuration(
        app,
        input_encoding='utf-8',
        output_encoding='utf-8',
        default_filters=['decode.utf8']
    )

    views_path = path.abspath(path.join(path.dirname(views.__file__)))
    mako_tmp_path = path.abspath(path.join(path.dirname(mako_tmp.__file__)))
    mako_lookup = TemplateLookup([views_path], module_directory=mako_tmp_path)

    index_template = mako_lookup.get_template('index.mak')
    login_template = mako_lookup.get_template('login.mak')
    mako_setup.put_template('index.mak', index_template)
    mako_setup.put_template('login.mak', login_template)

    # Configuring session
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    return app

run_app(make_app())
