import numpy as np

#read in data file input.txt
data = np.loadtxt('input.txt', dtype=int)

#calculate sum(abs(col1 - col2))
print(np.sum(np.abs(np.sort(data[:,0]) - np.sort(data[:,1]))))