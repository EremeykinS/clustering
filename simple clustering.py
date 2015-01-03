import sqlite3
import matplotlib
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import statistics

frame_len=5#00						#number of ticks in a frame
tail_len=5#0						#number of ticks in a 'tail'
n_f=900								#total number of frames
n_cl=50								#total number of clusters

class Frame(object):
	"""Frame class"""
	def __init__(self,id):
		self.id=id					#set id for the frame
		# self.fd=					#frame data

	def create(self):
		#creating frame and 'tail'
		self.con = sqlite3.connect('trades.db')#database connection
		self.cur = self.con.cursor()		#necessary!

		self.cur.execute("SELECT * FROM trades LIMIT {0} OFFSET {1}".format(frame_len,self.id))#select frame_len records with offset (for frame)
		self.con.commit()			#commit the request
		self.Rdata=self.cur.fetchall()#all SELECTed records (for frame)
		self.data=[row[1] for row in self.Rdata]#list of prices (for frame)

		self.cur.execute("SELECT * FROM trades LIMIT {0} OFFSET {1}".format(tail_len,self.id+frame_len))#select tail_len records with offset (for 'tail')
		self.con.commit()			#commit the request
		self.Tdata=self.cur.fetchall()#all SELECTed records (for 'tail')
		self.tail=[row[1] for row in self.Tdata]#list of prices (for 'tail')

		self.con.close()			#close database connection


# k_means = cluster.KMeans(n_clusters=n_cl)
# k_means.fit(data)

# cl=[[data[i] for i in range(0,n_f) if k_means.labels_[i]==j] for j in range(1,n_cl)]#Clusters

# for cln in range(n_cl-1):
# 	clt=list(map(list, zip(*cl[cln])))#Transposing
# 	clm=list(map(statistics.mean,clt))#Mean
# 	plt.plot(clm)
# 	plt.savefig("/home/es/Python_code/Clustering/img/mean{0:0>3}.png".format(cln+1), bbox_inches='tight')
# 	plt.close()

F=[]

for i in range(0,5):
	F.append(Frame(i))
	F[-1].create()
	print(F[-1].data)
print("-----------------------------------\n"+str(F[0].tail))