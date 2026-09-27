import numpy as np 

X = np.array([
    [2,5],
    [4,6],
    [6,8],
    [8,7]
])

W1 = np.array([
    [0.5,0.2,0.4],
    [0.3,0.8,0.1]
])
b1 = np.array([1,-2,0.5])
W2 = np.array([
    [0.7],
    [0.4],
    [0.6]
])
b2 = np.array([-1])

Z = (X@W1)+b1
print("Hidden layer:")
print(Z)
ReLU = np.maximum(0, Z)
print(ReLU)
Z2 = (ReLU@W2)+b2
print("output Layer:")
print(Z2)
sigmoid = 1 / (1+ np.exp(Z2))
print("The output is :")
print(sigmoid)