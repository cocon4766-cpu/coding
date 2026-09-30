import numpy as np 

X = np.array([1.0,2.0,3.0])
y_true = np.array([3.0,5.0,7.0])
W = 0.5
b = 0.0
learning_rate = 0.01

prediction = np.dot(X,W)+b
print(prediction)
MSE = np.mean((y_true-prediction)**2)
print(MSE)
gradient_W = (-2/len(X))*np.dot(X, (y_true-prediction))
print(gradient_W)
gradient_b = (-2/len(X))*np.sum(y_true-prediction)
print(gradient_b)  
W2 = W - learning_rate * gradient_W
print(W2)
b2 = b - learning_rate * gradient_b
print(b2)
new_prediction = np.dot(X,W2)+b2
print(new_prediction)
MSE2 = np.mean((y_true-new_prediction)**2)
print(MSE2)