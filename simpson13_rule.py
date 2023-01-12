# Python code for simpson's 1 / 3 rule
import math
import numpy as np
 
# Function to calculate f(x)
def func( x ):
    return math.log(x)
 
# Function for approximate integral
def simpsons_( ll, ul, n ):
 
    # Calculating the value of h
    h = ( ul - ll )/(n-1)
 
    # List for storing value of x and f(x)
    x = list()
    fx = list()
     
    # Calculating values of x and f(x)
#    i = 0
#    while i<= n:
#        x.append(ll + i * h)
#        fx.append(func(x[i]))
#        i += 1
    #OR
    x = np.linspace(ll, ul, n)
    fx =  (-1, 2, 23, 86, 215, 434, 767, 1238, 1871, 2690, 3719)

    # Calculating result
    res = 0
    i = 0
    while i< n:
        if i == 0 or i == n-1:
            res = res + fx[i]
        elif i % 2 != 0:
            res = res + 4*fx[i]
        else:
            res = res + 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res
     
# Driver code
lower_limit = 0  # Lower limit
upper_limit = 10 # Upper limit
n = 11 # Number of interval
print("%.6f"% simpsons_(lower_limit, upper_limit, n))