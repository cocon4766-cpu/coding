import numpy as np

X = np.array([
[2,5],
[4,6],
[6,8],
[8,7]
])
W = np.array([
    [0.5,0.3],
    [0.2,0.8]
])
bias = np.array([1,2])
Z = (X@W)+ bias
A = np.maximum(0,Z)
print(Z)
print(A)