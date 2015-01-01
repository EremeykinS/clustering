import sqlite3

con = sqlite3.connect('trades.db')
cur = con.cursor()

cur.execute("SELECT * FROM trades")
con.commit()
next_set=cur.fetchmany(10)
con.close()
print(next_set)