from aiohttp.web_exceptions import HTTPUnauthorized
from aiohttp_session import get_session

from blog import wsgi


def authorize(f):
    async def wrapper(*args, **kwargs):
        request = args[0]
        session = await get_session(request)
        if 'token' not in session or session['token'] != wsgi.config.get('token'):
            return HTTPUnauthorized()
        return f(*args, **kwargs)
    yield from wrapper
