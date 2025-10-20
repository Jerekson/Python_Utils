# pwd_store/bdd/SQLite
import sqlite3, logging, os, sys

log = logging.getLogger(__name__)

class SQL_config:
	def __init__(self, dbPath=os.path.dirname(os.path.realpath(__file__))+"/keystore.db"):
		log.debug("SQL_config instance created")
		log.debug("db name -> %s", dbPath)
		self.connection = None
		self.cursor = None
		self.dbName = dbPath
		self.dbexist = os.path.isfile(self.dbName)
		self.connect()
		if self.dbexist == False:
			self.create_schema()
		
	def save(self, password, pwdName):
		log.debug("methode save started")
		request = """INSERT INTO keystore(password, name)
				VALUES(?,?)"""
		try:
			self.cursor.execute(request, (password,pwdName))
		except sqlite3.ProgrammingError as e:
			log.error(e)
			log.debug("sqlite3 ProgrammingError \nCannot insert data %s due to \n%s", password, e)
			sys.exit()
		except sqlite3.IntegrityError as e:
			log.error(e)
			log.debug("sqlite3 IntegrityError \nCannot insert data %s due to \n%s", password, e)
			sys.exit()
		except sqlite3.OperationalError as e:
			log.error(e)
			log.debug("sqlite3 OperationalError \nCannot insert data %s due to \n%s", password, e)
			sys.exit()
		self.connection.commit()

	def create_schema(self):
		log.debug("create_schema started")
		try:
			self.cursor.execute("""CREATE TABLE keystore(
				id INTEGER PRIMARY KEY,
				password NOT NULL,
				name
				)""")
		except sqlite3.OperationalError:
			log.debug("Table 'keystore' already exists")
		log.info("DB keystore created")

	def connect(self):
		log.debug("connect mehode started")
		try:
			self.connection = sqlite3.connect(str(self.dbName))
			self.cursor = self.connection.cursor()
		except sqlite3.Error as e:
			log.error("error during the connection \n%s",e)
			sys.exit()
		log.info("connection established")

	def close_connection(self):
		self.connection.close()
		log.info("DB connection closed")

	def get_tables(self):
		log.debug("get tables start")
		for row in self.cursor.execute("SELECT name FROM sqlite_master"):
			print(row)

	def get_lines(self, tableName):
		log.debug("get all passwords")
		autorized_table = ['keystore']
		if tableName not in autorized_table:
			log.critical("try to get info from table %s", tableName)
			sys.exit()
		request = f"""SELECT * FROM {tableName}"""
		for row in self.cursor.execute(request):
			print(row)