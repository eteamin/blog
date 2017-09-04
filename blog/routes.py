from blog.controllers.root import index, admin, login, login_handler, submit_post


class Route:
    def __init__(self, method: str, path: str, handler: callable):
        self.method = method
        self.path = path
        self.handler = handler


def routes():
    # Declare application routes here
    return [
        Route('GET', '/', index),
        Route('GET', '/admin', admin),
        Route('POST', '/login_handler', login_handler),
        Route('GET', '/login', login),
        Route('POST', '/admin/submit_post', submit_post)
]
