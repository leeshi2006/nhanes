from copent import copent
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

csv1 = read_csv("~/your_dir/lab1.csv")
len = 100
csv1a = np.array(csv1)[0:len,:]
n = csv1a.shape[1]

# add noise
max1 = np.max(csv1a, axis = 0)
for i in range(0,n):
	csv1a[:,i] = csv1a[:,i] + np.random.normal(0,1,len) * max1[i] * 0.000005

mxce1 = np.zeros((n,n))
for i in range(0,n-1):
	for j in range(i+1,n):
		data1 = csv1a[:,[i,j]]
		mxce1[i,j] = copent(data1)
		mxce1[j,i] = mxce1[i,j]
		str1 = "(%d,%d) : %f" %(i,j,mxce1[i,j])
		print(str1)
	
plt.matshow(mxce1, cmap=plt.cm.Blues)
plt.show()
	
