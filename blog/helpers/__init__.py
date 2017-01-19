from aiohttp.web_exceptions import HTTPUnauthorized


def authorize(f):
    def wrapper(*args, **kwargs):
        request = args[0]
        if 'has_admin_permission' not in request.environ:
            return HTTPUnauthorized()
        if request.environ['has_admin_permission']:
            return HTTPUnauthorized()
        return f(*args, **kwargs)
    return wrapper
