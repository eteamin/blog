from aiohttp_mako import template


@template('index.mak')
async def root(request):
    return dict(ok=True)
