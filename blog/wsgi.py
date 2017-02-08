from os import path
import base64

from aiohttp_mako import setup, TemplateLookup
from aiohttp.web import Application, run_app

from cryptography import fernet
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import redis

from blog import views, mako_tmp
from blog.controllers.root import root, login, login_handler


app = Application()
app.router.add_route('GET', '/', root)
app.router.add_route('GET', '/login', login)
app.router.add_route('POST', '/login_handler', login_handler)

# Setup and configure Mako
mako_setup = setup(
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

connection = redis.StrictRedis()
# End of Mako configuration

# Configuring session
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
}
run_app(app)
