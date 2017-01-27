import numpy as np

### comTrapezoidArr
## Uses the composite trapezoidal method to numerically calculate
## an approximation of f's integral.
# f - a numpy array of f values 
# x - a numpy array of x value
def compTrapezoidArr(f, x):
    if f.shape != x.shape:
        print("The inputs are not the same size\n", "f.shape =", f.shape, 
                " x.shape =", x.shape)
        return;
    H = (x[4] - x[0]) / 5
    sum = 0
    for i in range(1, 4):
        sum += f[i]
    return (H * (( (f[0] + f[4]) / 2 ) + sum))

### compTrapezoid
## Uses the composite trapezoidal method to numerically calculate
## an approximation to a generic function over a range
# f - a function that returns a float
# a - the starting point as a float
# b - the end point as a float
# M - # of subdivisions
def compTrapezoid(f, a, b, M):
    H = (b - a) / M
    sum = 0
    for i in range(1, M):
        sum += f(a + i*H)
    return (H * (((f(a) + f(b)) / 2) + sum))

### compSimpson
## Uses the composite simpson method to numerically calculate
## an approximation to a generic function over a range
# f - a function that returns a float
# a - the starting point as a float
# b - the end point as a float
# M - # of subdivisions
def compSimpson(f, a, b, M):
    H = ((b - a) / M)
    sum = 0
    for i in range(1, M+1):
        x1 = a + (i-1)*H
        x2 = a + i*H
        sum += (f(x1) + 4 * f(mid(x1, x2)) + f(x2))
    return ( (H/6) * sum )

### mid
## helper function finds midpoint between x1 and x2
def mid(x1, x2):
    return ((x1 + x2) / 2)

def sin(x):
    return np.sin(x)

def findError(trueValue, approximation):
    return abs(trueValue - approximation)

f = np.array([10, 8, 7, 6, 5], dtype=np.float)
x = np.array([1, 5/4, 6/4, 7/4, 2], dtype=np.float)

# set up for question 1
eps = 10**(-12)

# True value of integral(sin(x), 0, np.pi) = 2
sinIntegral = 2.0

numIter = 100
err = 10
for i in (compTrapezoid, compSimpson):
    while err > eps:
        err = findError(sinIntegral, i(sin, 0, np.pi, numIter))
        numIter = numIter + 2
    print(i.__name__, "used approximately", numIter, "subdivisions to complete", "and achieved an error of", err)
    err = 10
    numIter = 100
