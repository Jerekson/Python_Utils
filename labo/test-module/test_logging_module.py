import logging, os
from pathlib import Path

# get where the script is
findmydir = os.path.dirname(os.path.realpath(__file__))

# adjusting the log level, from debug to critical (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(
	# Logging to a file
	filename=findmydir + "/test_logging_module.log",
	encoding="utf-8",
	filemode="a",

	# Logging Format
	format="{asctime} - {levelname} - {message}",
	style="{",
	datefmt="%Y-%m-%d %H:%M:%S",
	
	level=logging.DEBUG
)


# root logger 
logging.debug("test debug message")
logging.info("test info ?")
logging.warning("test warning")
logging.error("test error")
logging.critical("AAAAAAAH !!!")



# test exception & log
donuts = 5
guests = 0
try:
	donuts_per_guest = donuts / guests
except ZeroDivisionError:
	logging.error("DonutCalculationError", exc_info=True)




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
	package_logger.info("log configured")
	return package_logger