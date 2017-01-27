# Michael Stergianis (100568134)
import numpy as np

def strictDD(A):
    SDD = True
    for i in range(3):
        for k in range(0, 3):
            for l in range(0, 3):
                if k != l:
                    if ( A[k][l] >= A[i][i] ):
                        SDD = False
    return SDD


def gaussSeid(A, b, x0, tol, iter):
    test = True
    for i in range(0, 3):
        if abs(np.dot(A, x0)[i] - b[i]) >= tol:
            test = False
    if test:
        return (x0, iter)
    # x1 will take on the new values and be passed as x0 on next iteration
    x1 = np.array([0.0, 0.0, 0.0])
    sum1 = 0.0
    sum2 = 0.0
    for i in range(0, 3):
        for j in range(0, i):
            sum1 += (A[i][j] * x1[j])
        for k in range(i+1, 3):
            sum2 += (A[i][k] * x0[k])
        x1[i] = ((1 / A[i][i]) * (0 - sum1 - sum2 + b[i]))
        sum1 = 0.0
        sum2 = 0.0
    print("--------------------------------------------------------------")
    print("x0 = ", x0, " x1 = ", x1, " A[i][i] = {0:+f}\n".format(A[i][i]), 
            " b = ", b[i], " sum1 = ", sum1, " sum2 = ", sum2, " iter = ", iter)
    print("--------------------------------------------------------------")
    return gaussSeid(A, b, x1, tol, iter+1)
    


A = np.array([[3, -1, 1], [1, -3, -1], [1, 3, 5]])
b = np.array([0, -4, 2])

x0 = np.array([0, 0, 0])

tol = 10**-7

## if A is not SDD send a message
if not strictDD(A):
    print("A is not Strictly Diagonally Dominant")

# solve using np.linalg.solve, built in function to compare result
print("True result from numpy's built in functions", np.linalg.solve(A, b))
# my solution using Gauss-Seidel method
print(gaussSeid(A, b, x0, tol, 0))

