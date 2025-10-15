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
 
	try:
		cur.execute("CREATE TABLE meguitares(brand, model, year, origin)")
	except sqlite3.OperationalError:
		print("table already exists")


def multithreads_tests(whereIam):
	pass

def nosqli(whereIam):
	pass

def trigger_tests(whereIam):
	pass


# firsts_tests(whereIam)
primarykey_tests(whereIam)