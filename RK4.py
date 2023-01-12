def f(x,y): 
    return 4*(x**3) + 3*(x**2) + 2*x + 1
def k1(x,y): 
    return f(x,y)
def k2(x,y,h): 
    return f(x + h/2, y + (h/2)*k1(x,y))
def k3(x,y,h):
    return f(x + h/2, y + (h/2)*k2(x,y,h))
def k4(x,y,h):
    return f(x + h, y + h*k3(x,y,h))

def Rk4(yi,h,b,x):

    while x < b: 
        yi = yi + (h/6)*(k1(x,yi) + 2*k2(x,yi,h)+2*k3(x,yi,h)+ k4(x,yi,h))
        x = x + h

    print(yi)
    return 0

yi = 0
h = 1
b = 10
x = 0 
Rk4(yi,h,b,x)