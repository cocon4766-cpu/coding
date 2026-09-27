import numpy as np 

actual = np.array([10,20,30,40,50])
model_A = np.array([12,18,33,37,52])
model_B = np.array([15,19,25,45,48])
Errors_of_A = actual - model_A
print("The Errors of A are:")
print(Errors_of_A)
Square_of_Error_of_A = np.square(Errors_of_A)
print("The square of those errors are:")
print(Square_of_Error_of_A)
MSE_of_A =  sum(Square_of_Error_of_A)/len(Square_of_Error_of_A)
print("The MSE of A is:")
print(MSE_of_A)

Errors_of_B = actual - model_B
print("The Errors of B are:")
print(Errors_of_B)
Square_of_Error_of_B = np.square(Errors_of_B)
print("The square of those errors are:")
print(Square_of_Error_of_B)
MSE_of_B =  sum(Square_of_Error_of_B)/len(Square_of_Error_of_B)
print("The MSE of B is:")
print(MSE_of_B)