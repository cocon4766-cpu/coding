import numpy as np

X = np.array([
    [2,5],
    [4,6],
    [6,8]
])
W = np.array([
    [0.5,0.2],
    [0.3,0.8]
])
b1 = np.array([1,1])
Z1 = np.dot(X,W)+b1
print(Z1)
A1 = np.maximum(0,Z1)
W2 = np.array([
    [0.7],
    [0.4]
])
b2 = np.array([0.5])
Z2 = np.dot(A1,W2)+b2
print(Z2)