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
