# pwd_generator/__init__.py

__version__ = "0.1"

print("__init__ auto started - V:" + __version__)

from .pwd_generator import PWD_generator
from .bdd import SQL_config
from .utils import logging_setup