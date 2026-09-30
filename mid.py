import numpy as np

y_true = np.array([1,0,1,0])
pred_A = np.array([0.9,0.1,0.7,0.2])
pred_B = np.array([0.6,0.4,0.8,0.3])
BCE_of_A = -np.mean(y_true*np.log(pred_A)+(1-y_true)*np.log(1-pred_A))
print(BCE_of_A)
BCE_of_B = -np.mean(y_true*np.log(pred_B)+(1-y_true)*np.log(1-pred_B))
print(BCE_of_B)
Differenc_in_A_and_B = BCE_of_B - BCE_of_A
print(Differenc_in_A_and_B)