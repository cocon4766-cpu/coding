import numpy as np 

X = np.array([-30,-1,0,10,30])
sigmoid = 1/ (1+(np.exp(-X)))
ReLU = np.maximum(0,X)
print(sigmoid)
print(ReLU)