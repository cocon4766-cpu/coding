import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("The sum of r1 is:",np.sum(A[0]))
print("The sum of r2 is:",np.sum(A[1]))
print("The sum of r3 is:",np.sum(A[2]))
print("The sum of c1 is:",np.sum(A[:,0]))
print("The sum of c2 is:",np.sum(A[:,1]))
print("The sum of c3 is:",np.sum(A[:,2]))
print("The mean of r1 is:",sum(A[0]/len(A[0])))
print("The mean of r2 is:",sum(A[1]/len(A[1])))
print("The mean of r3 is:",sum(A[2]/len(A[2])))
print("The mean of c1 is:",sum(A[:,0]/len(A[:,0])))
print("The mean of c2 is:",sum(A[:,1]/len(A[:,1])))
print("The mean of c3 is:",sum(A[:,2]/len(A[:,2])))