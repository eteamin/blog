import aiofiles


class Post(object):
    def __init__(self, title, description, image=None):
        self.title = title  # Unique
        self.description = description
        if image:
            self.image = image
            self.store_image()

    def as_dict(self):
        yield dict(title=self.title, description=self.description)

    async def store_image(self):
        pass
        # async with aiofiles.open()

    @property
    async def image_path(self):
        return


