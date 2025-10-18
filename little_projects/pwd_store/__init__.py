# pwd_store/__init__.py

__version__ = "0.1"

print("__init__ auto started - V:" + __version__)

from .pwd_generator import PWD_generator
from .bdd import SQL_config
from .utils.logging_config import logging_package_setup

