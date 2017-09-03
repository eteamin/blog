from os import path
import json

import aiofiles


STORAGE = path.abspath(path.join(path.dirname(__file__), '..', 'public', 'storage'))


class Post(object):
    def __init__(self, title, description, image=None):
        self.title = title  # Unique
        self.description = description
        self.image = image

    def as_string(self):
        return json.dumps(dict(title=self.title, description=self.description, image=True if self.image else False))

    async def store_image(self):
        if self.image:
            async with aiofiles.open(self.image_path, 'wb') as stored_image:
                while True:
                    chunk = self.image.file.read(1024)
                    if not chunk:
                        break
                    await stored_image.write(chunk)

    @property
    def image_path(self):
        return '{}/{}'.format(STORAGE, self.title)
