import numpy as np

#read in data file input.txt
data = np.loadtxt('./../input.txt', dtype=int)

count = 0
for i in range(0, len(data[:,0])):
    if data[i,0] in data[:,1]:
        count += data[i,0] * (np.count_nonzero(data[:,1] == data[i,0]))

print(count)