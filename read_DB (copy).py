import sqlite3
import matplotlib
from sklearn import cluster, datasets

con = sqlite3.connect('trades.db')
cur = con.cursor()
cur.execute("SELECT * FROM trades")
con.commit()

next_set=cur.fetchmany(10)

#print(next_set)
#print([next_set[i][2] for i in range(len(next_set))])
print([row[1]-next_set[0][1] for row in next_set])

con.close()