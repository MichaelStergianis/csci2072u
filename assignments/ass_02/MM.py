## Michael Stergianis (100 568 134) ##


real_r = 1.3027756377319945624
# Our function (2x^3) + (4x^2) - (4x) - 6
def f(x):
    return 2*x**3 + 4*x**2 - 4*x - 6

# find a standard secant
def div_diff_2(f, x0, x1):
    return (f(x1) - f(x0)) / (x1 - x0)

# Divided difference for three values
def div_diff_3(f, x0, x1, x2):
    fx1 = f(x1)
    return ( ( (f(x2) - fx1)/((x2 - x1) * (x2 - x0)) ) -  ( (fx1 - f(x0))/((x1 - x0) * (x2 - x0)) ) )

# definition of w value, makes for a neater MM function
def w(f, x0, x1, x2):
    return ( div_diff_2(f, x2, x1) + div_diff_2(f, x2, x0) - div_diff_2(f, x1, x0) )

### Muller's Method ###
## Takes input parameters, spits out the closest solution of the function
## f    -- the function in question
## x0   -- the first x input
## x1   -- the second x input
## x2   -- the third and in our case final x input
## iter -- the number of iterations (minimum 0 for three guesses)
def MM(f, x0, x1, x2, iter):
    assert(iter >= 0)
    if iter == 0:
        # f(x2) gets used a lot, calc once use many. same with wf
        f2 = f(x2)
        wf = w(f, x0, x1, x2)
        f3 = div_diff_3(f, x0, x1, x2)
        # calculate both b +- (b^2 - 4ac) to find largest denominator
        # save both as we will use 1 of them again
        wminu = (wf - (wf**2 - 4*f2*f3)**(.5))
        wplus = (wf + (wf**2 - 4*f2*f3)**(.5))
        # depending on which is the larger value we will use that one to calculate
        # xk, return that value
        if ( abs(wminu) > abs(wplus) ):
            ans = ( x2 - (2 * f2 / (wminu)) )
        else:
            ans = ( x2 - (2 * f2 / (wplus)) )
        print "{0:1.19f} {1:1.7e}".format(ans, abs(ans - real_r)) 
        return ans
    else:
        swap = x0
        x0 = x1
        x1 = x2
        x2 = MM(f, swap, x0, x1, iter-1)
        # call function with iter = 0, this will give our answer to x2 for any previous calls
        return MM(f, x0, x1, x2, 0)
        
print "{0:>21s} {1:>13s}".format('calculated root', 'err')
r = MM(f, 1.1, 1.3, 1.5, 3)
print "-------- Final Answer --------"
print r
###### For 9 if you wish to try
####print "{0:>21s} {1:>13s}".format('calculated root', 'err')
####r = MM(f, 1.1, 1.3, 1.5, 9)
####print "-------- Final Answer --------"
####print r
