import numpy as np

# input a from given values
A = np.array([[1,1,1,0],[1,2,0,1],[1,3,0,0],[1,4,0,0]])

# define b as a 1,4 vector
b = np.array([145, 270, 400, 510])
# then reshape as a 4,1 vector
b = b.reshape(4,1)

# built in qr factorization
q, r = np.linalg.qr(A, mode='full')

q = q*-1
r = r*-1

print(q)
print(r)

# built in dot product and q.T is q transpose
d = np.dot(q.T, b)

print(d)

d = d[0:2]

print(d)

r = r[0:2,0:2]

print(r)

# now to find a and b

x = [0, 0]
# b = d[1,0] / r[0, 1]
x[1] = d[1,0] / r[1, 1]
print( "b = " , x[1])

# a = (d[0,0] - 5 * x[1]) / 2
print(d[0,0])
print(x[1])
x[0] = (d[0,0] - (5 * x[1])) / 2
print("a = ", x[0])
