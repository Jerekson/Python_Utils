import sqlite3, os

whereIam = os.path.dirname(os.path.realpath(__file__))

def firsts_tests(whereIam):
	# create new connexion to the BDD, it create it if it's not already created. 
	con = sqlite3.connect(whereIam+"/test_sqlite3_module.db")

	# create the cursor
	cur = con.cursor()

	# Create the first table. 
	try:
		cur.execute("CREATE TABLE movie(title, year, score)")
	except sqlite3.OperationalError:
		print("table 'movie' already exists")

	# get this last table 
	res = cur.execute("SELECT name FROM sqlite_master")
	print("tables :\n", res.fetchone())

	# INSERT lines
	cur.execute("""INSERT INTO movie VALUES 
		('Movie 1', 1955, 8.2),
		('MOvie 2', 2010, 4)
		""")

	# commit all changes 
	con.commit()

	res = con.execute("SELECT score FROM movie")
	print(res.fetchall())

	# INSERT a list from dict
	data = [
	("Movie 3", 1999, 9),
	("Movie 4", 2008, 4),
	("Movie 5", 1982, 6.7)
	]

	# INSERT theses lines and best pratice with params
	cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
	con.commit()

	for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
		print(row)

	# close the connexion 
	con.close()

	# new connexion
	newcon = sqlite3.connect(whereIam+"/test_sqlite3_module.db")
	newcur = newcon.cursor()
	print(newcon.execute("SELECT title, year FROM movie ORDER BY score DESC").fetchone())
	newcon.close()


# new tests with an other table 
def primarykey_tests(whereIam):
	con = sqlite3.connect(whereIam+"/test_sqlite3_module.db")
	cur = con.cursor()

	data1 = [
	(1, 'fname1', 'lname1'),
	(2, 'fname2', 'lname2'),
	]
	data2 = [
	('fname3','lname3'),
	('fname4','lname4')
	]

	# primary key with auto increment
	try:
		cur.execute("""CREATE TABLE users(
			id INTEGER PRIMARY KEY,
			fname NOT NULL,
			lname NOT NULL
			)
			""")
	except sqlite3.OperationalError:
		print("table 'users' already exists")

	try:
		con.executemany("INSERT INTO users VALUES(?,?,?)", data1)
	except sqlite3.ProgrammingError as e:
		print(e)
	except sqlite3.IntegrityError as e:
		print(e) 
	except sqlite3.OperationalError as e:
		print(e)
	
	try:
		con.executemany("INSERT INTO users(fname, lname) VALUES(?,?)", data2)
	except sqlite3.ProgrammingError as e:
		print(e)
	except sqlite3.OperationalError as e:
		print(e)

	con.commit()
	res = con.execute("SELECT * FROM users")
	for row in res:
		print(row)



def m_2ultithreads_tests(whereIam):
	pass

def nosqli(whereIam):
	pass

def trigger_tests(whereIam):
	pass

def dropTable(whereIam, dbName, tableName):
	con = sqlite3.connect(whereIam+"/"+dbName)
	cur = con.cursor()
	cur.execute("DROP TABLE "+ tableName)
	cur.close()

def get_all_tables(whereIam, dbName):
	print("-- get all tables function start --")
	con = sqlite3.connect(whereIam+"/"+dbName)
	cur = con.cursor()
	for row in cur.execute("SELECT name FROM sqlite_master"):
		print(row[0])
	con.close()
	print("-- get all tables function end --")


get_all_tables(whereIam, "test_sqlite3_module.db")
# firsts_tests(whereIam)
primarykey_tests(whereIam)


# dropTable(whereIam, 'test_sqlite3_module.db', 'meguitares')
dropTable(whereIam, 'test_sqlite3_module.db', 'users')
# dropTable(whereIam, 'test_sqlite3_module.db', 'users_2')