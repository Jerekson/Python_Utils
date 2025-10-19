# pwd_store/bdd/SQLite
import sqlite3, logging

log = logging.getLogger(__name__)

class SQL_config:
	def __init__(self, dbPath=".testDB.b"):
		log.debug("SQL_config instance created")
		log.debug("db name is %s", dbPath)
		
	
	def run(self):
		return "sqlconfig def Run started"

	def createDB(dbname):
		return "createDB started"