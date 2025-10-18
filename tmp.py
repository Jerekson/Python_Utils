from little_projects.pwd_store import PWD_generator, SQL_config, logging_package_setup
import logging

newpwd = PWD_generator.get_new_pwd("ask for new")
print(newpwd)

gestion = SQL_config.run("test")
print(gestion)
logging_package_setup()
logger = logging.getLogger(__name__)
logger.info("test")