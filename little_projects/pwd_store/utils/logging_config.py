import logging, sys

# Logger Name 
PACKAGE_LOGGER_NAME = "pwd_store"

# FilePath == None for default
# loglevel == 
def logging_setup():
	print("logging setup alive")


# Logging infos -> 
# type -> stream (for prompt) or set a filePath
def logging_setup_stream(level=logging.INFO, handler_type='stream'):
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
    
	# Récupère le logger racine de votre package (ou le root logger)
	package_logger = logging.getLogger('little_projects.pwd_store')
	package_logger.setLevel(level)
	package_logger.addHandler(handler)
	package_logger.propagate = False # Évite la double émission si le root logger est aussi configuré

	# Log pour confirmer le démarrage (utilisez le logger du package)
	package_logger.info("Configuration de logging personnalisée démarrée.")
	return package_logger


def add_null_handler():
	return "add null handler alive"