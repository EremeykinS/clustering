import sqlite3
import matplotlib
from sklearn import cluster, datasets
import matplotlib.pyplot as plt

con = sqlite3.connect('trades.db')
cur = con.cursor()
cur.execute("SELECT * FROM trades")
con.commit()

frame_len=600
n_f=900
n_cl=110

data=[-1 for i in range(0,n_f)]

for i in range(0,n_f):
	next_set=cur.fetchmany(frame_len)
	data[i]=[row[1]-next_set[0][1] for row in next_set]
	# data[i]=[row[1] for row in next_set]
con.close()
#print([next_set[i][2] for i in range(len(next_set))])
#print(data)



k_means = cluster.KMeans(n_clusters=n_cl)
k_means.fit(data)
# print(k_means.labels_)

# cl_1=[data[i] for i in range(0,n_f) if k_means.labels_[i]==1]
cl=[[data[i] for i in range(0,n_f) if k_means.labels_[i]==j] for j in range(1,n_cl)]

# for j in range(0,n_cl-1):
# 	print(len(cl[j]))
# print(cl)

# tt=[10,20,30,30,20,10]

print(min(10,len(cl[1])))

for j in range(1,min(20,len(cl[1]))):
	plt.plot(cl[1][j])

plt.show()
