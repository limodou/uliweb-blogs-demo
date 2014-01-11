import uliweb
from uliweb.utils.setup import setup
import apps

__doc__ = """doc"""

setup(name='uliweb_blogs',
    version=apps.__version__,
    description="Description of your project",
    package_dir = {'uliweb_blogs':'apps'},
    packages = ['uliweb_blogs'],
    include_package_data=True,
    zip_safe=False,
)
