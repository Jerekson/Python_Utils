import logging, sys, importlib 
from pathlib import Path
from logging import NullHandler
from datetime import datetime

def add_null_handler():
	logger = logging.getLogger("ToDoList")
	if not logger.handlers: # check if the logger has already a handler 
		logger.addHandler(NullHandler())

class CustomFormatter(logging.Formatter):

    blue = "\x1b[34m"
    cyan = "\x1b[36m"
    green = "\x1b[32m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" #(%(filename)s:%(lineno)d)

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def logging_setup(level=logging.INFO, handler_type="stream"):
    # Cancel if it's already configured
    if logging.getLogger().handlers:
        return
    
    # Create the format
    log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    # handler prompt or file (default = prompt)
    if handler_type == "stream":
        handler = logging.StreamHandler(sys.stdout)
    else:
        # get the logs directorie path and create the log file name (today year - today month . log) 
        package_root_path = Path(__file__).resolve().parent.parent
        package_root_name = package_root_path.name
        date_now = str(datetime.now().year) + "-" + str(datetime.now().month)
        log_file_name = date_now + ".log"
        log_dir_path = package_root_path / "logs" / log_file_name

        handler = logging.FileHandler()

    # handler.setFormatter(log_format)
    handler.setFormatter(CustomFormatter())
    
    # Retrieve the package root logger
    package_logger = logging.getLogger("ToDoList")
    package_logger.setLevel(level)
    package_logger.addHandler(handler)
    package_logger.propagate = False # avoids double emission

    # return the package logger
    package_logger.debug("Log configured")
    return package_logger
