import numpy as np

x = np.array([[4,-1,1],[4,-8,1],[-2,1,5]], dtype=('f8'))
b = b = np.array([7, -21, 15])

u = np.zeros((3, 3))
l = np.zeros((3, 3))
d = np.zeros((3, 3))

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if j > i:
            u[i][j] = x[i][j]
        elif j < i:
            l[i][j] = x[i][j]
        else:
            d[i][j] = x[i][j]

print(u, '\n')
