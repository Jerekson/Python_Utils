import sqlite3

con = sqlite3.connect(".test_sqlite3_module.db")
cur = con.cursor()
print(cur)
cur.execute("CREATE TABLE movie(title, year, score)")