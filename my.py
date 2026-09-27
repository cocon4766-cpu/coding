import numpy as np

data = np.array([
                 [2,5],
                 [4,6],
                 [6,7],
                 [8,9],
                 [10,8]
])
print(data.shape[0])
print(np.shape(data))
print(data[:,0])
print(data[:,1])
average= data.mean(axis=0)
print(average)
