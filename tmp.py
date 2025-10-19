from little_projects.pwd_store import PWD_generator, SQL_config, logging_package_setup
import logging

logging_package_setup(level=logging.DEBUG)
generator = PWD_generator()
sqltest = SQL_config()