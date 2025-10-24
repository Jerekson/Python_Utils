import logging, sys
from logging import NullHandler

# Logger Name 
PACKAGE_LOGGER_NAME = "pwd_store"

# Logging infos -> 
# type -> stream (for prompt) or set a filePath
def logging_package_setup(level=logging.INFO, handler_type='stream'):
	# cancel if it's already configured
	if logging.getLogger().handlers:
		return
		
	# create the format (LIKE basicConfig)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# the handler, prompt or file
	if handler_type == 'stream':
		handler = logging.StreamHandler(sys.stdout)
	else:
		handler = logging.FileHandler('pwd_store.log')

	handler.setFormatter(formatter)
    
	# retrieve the root logger from the package
	package_logger = logging.getLogger('little_projects.pwd_store')
	package_logger.setLevel(level)
	package_logger.addHandler(handler)
	package_logger.propagate = False # avoids double emission if the root logger already configured

	# alive the return the package_logger
	package_logger.debug("log configured")
	return package_logger

def add_null_handler():
	logger = logging.getLogger("little_projects.pwd_store")
	if not logger.handlers: # check if the logger has already a handler 
		logger.addHandler(NullHandler())