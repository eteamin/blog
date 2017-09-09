from blog.controllers.root import index, admin, login, login_handler, submit_post, single


class Route:
    def __init__(self, method: str, path: str, handler: callable):
        self.method = method
        self.path = path
        self.handler = handler


class Resource:
    def __init__(self, path: str, route: Route):
        self.path = path
        self.route = route


def resources():
    return [
        Resource('/posts/{posts_title}', Route('GET', '/posts/', single)),
    ]


def routes():
    # Declare application routes here
    return [
        Route('GET', '/', index),
        Route('GET', '/admin', admin),
        Route('POST', '/login_handler', login_handler),
        Route('GET', '/login', login),
        Route('POST', '/admin/submit_post', submit_post),
        Route('GET', '/posts', single)
]
