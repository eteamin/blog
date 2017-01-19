

class Post(object):
    def __init__(self, title, details, image=None):
        self.title = title
        self.details = details
        self.image = image

    def __repr__(self):
        return self.title
