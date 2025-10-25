import logging, sys, importlib 
from pathlib import Path
from logging import NullHandler
from datetime import datetime

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
        # get the logs directorie path and create the log file name (today year - today month . log) 
        package_root_path = Path(__file__).resolve().parent.parent
        package_root_name = package_root_path.name
        date_now = str(datetime.now().year) + "-" + str(datetime.now().month)
        log_file_name = date_now + ".log"
        log_dir_path = package_root_path / "logs" / log_file_name

        handler = logging.FileHandler()

    handler.setFormatter(log_format)

    # Retrieve the package root logger
    package_logger = logging.getLogger("little_projects.ToDoList")
    package_logger.setLevel(level)
    package_logger.addHandler(handler)
    package_logger.propagate = False # avoids double emission

    # return the package logger
    package_logger.debug("Log configured")
    return package_logger
