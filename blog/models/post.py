

class Post(object):
    def __init__(self, title, details, image=None):
        self.title = title  # Unique
        self.details = details
        self.image = image

    def as_dict(self):
        yield dict(title=self.title, details=self.details)
