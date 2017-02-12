import aiofiles

from blog import wsgi


class Post(object):
    def __init__(self, title, description, image=None):
        self.title = title  # Unique
        self.description = description
        if image:
            self.image = image
            self.store_image()

    def as_dict(self):
        yield dict(title=self.title, description=self.description, image_path=self.image_path)

    async def store_image(self):
        async with aiofiles.open(self.image_path, 'wb') as stored_image:
            while True:
                chunk = await self.image.file.read()
                if not chunk:
                    break
                await stored_image.write(chunk)

    @property
    def image_path(self):
        return '{}/{}'.format(wsgi.storage_path, self.image.name)
