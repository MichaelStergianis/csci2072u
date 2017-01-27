# Assignment 3 Michael Stergianis (100568134)
# All solutions will assume a 3x3 matrix with a 1x3 solution
import numpy as np

def gaussElim(A, b):
    # make an augmented matrix from the variables and solution
    C = np.concatenate((A, b.T), axis=1)
    
    # subtract a_0_i from rows 1 and 2
    for i in reversed(range(0, 4)):
        C[1][i] = C[1][i] - (C[0][i] * (C[1][0] / C[0][0]))
    for i in reversed(range(0, 4)):
        C[2][i] = C[2][i] - (C[0][i] * (C[2][0] / C[0][0]))

    # subtract to make a_21 0 isolating for x3
    for i in reversed(range(1, 4)):
        C[2][i] = C[2][i] - (C[1][i] * (C[2][1] / C[1][1]))
        
    # start isolating for variables x3 first
    x3 = C[2][3] / C[2][2]
    x2 = (C[1][3] - (x3 * C[1][2])) / C[1][1]
    x1 = (C[0][3] - ( (x2 * C[0][1]) + (x3 * C[0][2]) )) / C[0][0]
    x = np.array([[x1, x2, x3]])
    return x

def partPivot(A, b):

    return

A = np.array([[2.101,  -23510,   11.4451], 
              [1.4321, -41.320, -13.1456], 
              [0.3443,  6.3277,  1.255]])
b = np.array([[-11325, 28.723, -7.254]])

# Print the absolute solution, from a built in function in numpy.
# not to be confused with my solutions
print("############## SOLUTION ######################")
print(np.linalg.solve(A, b.T),)
print("##############    END   ######################\n")

x_gauss = gaussElim(A, b)
