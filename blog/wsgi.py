from os import path

from aiohttp_mako import setup, TemplateLookup
from aiohttp.web import Application, run_app

from blog import views, mako_tmp
from blog.controllers.root import root


app = Application()
app.router.add_route('GET', '/', root)

# Setup and configure Mako
mako_setup = setup(
    app,
    input_encoding='utf-8',
    output_encoding='utf-8',
    default_filters=['decode.utf8']
)

views_path = path.abspath(path.join(path.dirname(views.__file__)))
mako_tmp_path = path.abspath(path.join(path.dirname(mako_tmp.__file__)))
mako_lookup = TemplateLookup([views_path], module_directory=mako_tmp_path)

index = mako_lookup.get_template('index.mak')
mako_setup.put_template('index.mak', index)

# End of Mako configuration
run_app(app)
