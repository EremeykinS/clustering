import sqlite3
import matplotlib
from sklearn import cluster, datasets

con = sqlite3.connect('trades.db')
cur = con.cursor()
cur.execute("SELECT * FROM trades")
con.commit()

frame_len=33
n_f=100

data=[-1 for i in range(0,n_f)]

for i in range(0,n_f):
	next_set=cur.fetchmany(frame_len)
	data[i]=[row[1]-next_set[0][1] for row in next_set]

#print([next_set[i][2] for i in range(len(next_set))])
#print(data)

k_means = cluster.KMeans(n_clusters=8)
k_means.fit(data)
print(k_means.labels_)

con.close()