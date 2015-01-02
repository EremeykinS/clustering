import sqlite3
import matplotlib
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import statistics

con = sqlite3.connect('trades.db')
cur = con.cursor()
cur.execute("SELECT * FROM trades")
con.commit()

frame_len=500
n_f=900
n_cl=50

data=[-1 for i in range(0,n_f)]

for i in range(0,n_f):
	next_set=cur.fetchmany(frame_len)
	data[i]=[row[1]-next_set[0][1] for row in next_set]
con.close()

k_means = cluster.KMeans(n_clusters=n_cl)
k_means.fit(data)

cl=[[data[i] for i in range(0,n_f) if k_means.labels_[i]==j] for j in range(1,n_cl)]#Clusters

# for j in range(0,n_cl-1):
# 	print(len(cl[j]))
# print(cl)

for cln in range(n_cl-1):
	clt=list(map(list, zip(*cl[cln])))#Transposing
	clm=list(map(statistics.mean,clt))#Mean
	plt.plot(clm)
	plt.savefig("/home/es/Python_code/Clustering/img/mean{0:0>3}.png".format(cln+1), bbox_inches='tight')
	plt.close()
#