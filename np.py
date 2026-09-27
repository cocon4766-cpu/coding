import numpy as np

X = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [2,4,6]
])
W1 = np.array([
    [0.2,0.5],
    [0.4,0.3],
    [0.6,0.1]
])
b1 = np.array([1,2])
W2 = np.array([
    [0.7],
    [0.9]
])
b2 = np.array([1])

Z1 = (X@W1)+b1
print("Input layer:")
print(Z1)
A1 = np.maximum(0,Z1)
print("Hidden layer:")
print(A1)
Z2 = (A1@W2)+b2
print("Output layer:")
print(Z2)
print("The shape of the output layer:")
print(np.shape(Z2))