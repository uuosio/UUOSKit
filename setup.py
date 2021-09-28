from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="eoskit",
    version="0.8.6",
    description="Python Toolkit for EOSIO",
    author='The UUOSIO Team',
    license="MIT",
    packages=['eoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'eoskit': 'pysrc'},
    package_data={'eoskit': ['data/*']},
    install_requires=[
        'urllib3>=1.21.1',
        'certifi',
        'toolz',
        'funcy',
        'prettytable',
        'requests_unixsocket'
    ],
    include_package_data=True
)
