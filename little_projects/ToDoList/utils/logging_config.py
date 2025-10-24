import logging, sys
from pathlib import Path
from logging import NullHandler

def add_null_handler():
	logger = logging.getLogger("little_projects.ToDoList")
	if not logger.handlers: # check if the logger has already a handler 
		logger.addHandler(NullHandler())

def logging_setup(level=logging.INFO, handler_type="stream"):
    # Cancel if it's already configured
    if logging.getLogger().handlers:
        return
    
    # Create the format
    log_format = logging.Formatter("%(acstime)s - %(name)s - %(levelname)s - %(message)s")
    
    # handler prompt or file (default = prompt)
    if handler_type == "stream":
        handler = logging.StreamHandler(sys.stdout)
    else: 
        # TODO : get Path to dirlog file 
        handler = logging.FileHandler()
