

class Post(object):
    def __init__(self, title, description, image=None):
        self.title = title  # Unique
        self.description = description
        self.image = image

    def as_dict(self):
        yield dict(title=self.title, description=self.description)
