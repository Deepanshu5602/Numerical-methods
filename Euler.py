def func( x, y ):
    return -(y**2)/(x**2)

# Function for euler formula
def euler( x0, y, h, x ):
    x_arr = []
    y_arr = []
    temp = -0 
    while x0 < x:        
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h 
        x_arr.append(x0)
        y_arr.append(y)
        #print("Euler's solution at x = ", x0, " is ", "%.6f"% y)
    return x_arr, y_arr  

import numpy as np
x0 = 1
y = 0.1
x = 10
h_arr = [2, 1, 0.5, 0.25, 0.1]

for i in range(len(h_arr)):
  print("For h = {}".format(h_arr[i]))
  print("Euler:")
  x_arr, y_arr = euler( x0, y, h_arr[i], x )
  print(np.array((x_arr, y_arr)).T)
  print("") 