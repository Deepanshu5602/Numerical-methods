# Implementation of matplotlib function       
import matplotlib.pyplot as plt 
def func( x, y ):
    return -(y**2)/(x**2)

#Euler Method

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

#RK4 Method
def f( x, y ):
    return -(y**2)/(x**2)

def k1(x,y): 
    return f(x,y)
def k2(x,y,h): 
    return f(x + h/2, y + (h/2)*k1(x,y))
def k3(x,y,h):
    return f(x + h/2, y + (h/2)*k2(x,y,h))
def k4(x,y,h):
    return f(x + h, y + h*k3(x,y,h))

def RK4(x, xn, y, h):
  x_arr = []
  y_arr = []
  while x < xn:     
    y = y + (h/6)*(k1(x,y) + 2*k2(x,y,h)+2*k3(x,y,h)+ k4(x,y,h))
    x = x + h
    x_arr.append(x)
    y_arr.append(y)
  return x_arr, y_arr


def raiston_method