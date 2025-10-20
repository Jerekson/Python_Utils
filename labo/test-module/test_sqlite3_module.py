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

	res = cur.execute("SELECT score FROM movie")
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
	print(newcur.execute("SELECT title, year FROM movie ORDER BY score DESC").fetchone())
	newcon.close()


# new tests with an other table 
def one_primarykey_tests(whereIam):
	con = sqlite3.connect(whereIam+"/test_sqlite3_module.db")
	cur = con.cursor()

	data1 = [
	(1, 'fname1', 'dataType1'),
	(2, 'fname2', 'dataType1'),
	]
	data2 = [
	('fname3','dataType2'),
	('fname4','dataType2')
	]

	# primary key with auto increment
	try:
		cur.execute("""CREATE TABLE users_onepkey(
			id INTEGER PRIMARY KEY,
			fname NOT NULL,
			lname NOT NULL
			)
			""")
	except sqlite3.OperationalError:
		print("table 'users_onepkey' already exists")

	try:
		cur.executemany("INSERT INTO users_onepkey VALUES(?,?,?)", data1)
	except sqlite3.ProgrammingError as e:
		print(e)
		print("\ndata1 type dont work")
	except sqlite3.IntegrityError as e:
		print(e)
		print("\ndata1 type dont work") 
	except sqlite3.OperationalError as e:
		print(e)
		print("\ndata1 type dont work")
	
	try:
		cur.executemany("INSERT INTO users_onepkey(fname, lname) VALUES(?,?)", data2)
	except sqlite3.ProgrammingError as e:
		print(e)
		print("\ndata2 type dont work")
	except sqlite3.OperationalError as e:
		print(e)
		print("\ndata2 type dont work")

	con.commit()
	res = cur.execute("SELECT * FROM users_onepkey")
	for row in res:
		print(row)


def two_primarykey_tests(whereIam):
	con = sqlite3.connect(whereIam+"/test_sqlite3_module.db")
	cur = con.cursor()

	data1 = [
	(1, 'fname1', 'dataType1'),
	(2, 'fname2', 'dataType1'),
	]
	data2 = [
	('fname3','dataType2'),
	('fname4','dataType2')
	]

	# primary key with auto increment
	try:
		cur.execute("""CREATE TABLE users_twopkey(
			id,
			fname,
			lname,
			PRIMARY KEY(id, lname)
			)
			""")
	except sqlite3.OperationalError:
		print("table 'users_twopkey' already exists")
	
	try:
		cur.executemany("INSERT INTO users_twopkey VALUES(?,?,?)", data1)
	except sqlite3.ProgrammingError as e:
		print(e)
		print("\ndata1 type dont work")
	except sqlite3.IntegrityError as e:
		print(e)
		print("\ndata1 type dont work") 
	except sqlite3.OperationalError as e:
		print(e)
		print("\ndata1 type dont work")
	
	try:
		cur.executemany("INSERT INTO users_twopkey(fname, lname) VALUES(?,?)", data2)
	except sqlite3.ProgrammingError as e:
		print(e)
		print("\ndata2 type dont work")
	except sqlite3.OperationalError as e:
		print(e)
		print("\ndata2 type dont work")
	
	con.commit()
	res = cur.execute("SELECT * FROM users_twopkey")
	for row in res:
		print(row)

def multithreads_tests(whereIam):
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
#firsts_tests(whereIam)
#one_primarykey_tests(whereIam)
#two_primarykey_tests(whereIam)


deleteall = False
deletemovie = False
deleteonekey = False
deletetwokey = False
if deleteall or deletemovie:
	try:
		dropTable(whereIam, 'test_sqlite3_module.db', 'movie')
	except:
		print("done for movie")
if deleteall or deleteonekey:
	try:
		dropTable(whereIam, 'test_sqlite3_module.db', 'users_onepkey')
	except:
		print("done for users_onepkey")
if deleteall or deletetwokey:
	try:
		dropTable(whereIam, 'test_sqlite3_module.db', 'users_twopkey')
	except:
		print("done for users_twopkey")

