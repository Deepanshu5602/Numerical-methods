import matplotlib.pyplot as plt
def der_x(x, y, t): 
    return y
def der_y(x, y, t): 
    return -x+t

def midpoint(x, y, t, h, t_final):
    x1 = []
    y1 = []
    while t < t_final:

        x_new = x + h * der_x(x + h/2, y + (h/2)*der_x(x, y, t), t)
        y_new = y + h * der_y(x + h/2, y + (h/2)*der_y(x, y, t), t)
        x1.append(x_new)
        y1.append(y_new)
        x = x_new 
        y = y_new
        t = t + h
    plt.plot(x1, y1)
    plt.show()
    return x_new, y_new, t,

def euler(x, y, t, h, t_final):
    while t < t_final:
        x_new = x + h * der_x(x, y, t) 
        y_new = y + h * der_y(x, y, t)
        x = x_new 
        y = y_new
        t = t + h
    return x_new, y_new, t

def raiston(x, y, t ,h, t_final): 
    while t < t_final:
        derx = der_x(x, y, t) 
        dery = der_y(x, y, t)
        x_new = x + (h/3)*(derx + 2*(der_x(x + (3/4)*h, y + (3/4)*h*derx, t)))
        y_new = y + (h/3)*(dery + 2*(der_y(x + (3/4)*h, y + (3/4)*h*dery, t)))
        x = x_new 
        y = y_new
        t = t + h
    return x_new, y_new, t

def heun(x, y, t, h, t_final):
    while t < t_final:
        temp1 = der_x(x, y, t)
        temp2 = der_y(x, y, t) 
        x_new = x + h*(temp1 + der_x(x + temp1 * h, y + temp2 * h, t+h))/2 
        y_new = y + h*(temp2 +der_y(x + temp1 * h,y + h*temp2,t+h))/2
        x = x_new
        y = y_new
        t = t + h 
    return x, y, t

def k1(x, y, t, der): 
    return der(x, y, t)
def k2(x, y, t, h, der):
    return der(x + h/2, y + h/2*k1(x, y, t, der), t)
def k3(x, y, t, h, der):
    return der(x + h/2, y + h/2*k2(x, y, t, h, der), t)
def k4(x, y, t, h, der):
    return der(x + h, y + h*k3(x, y, t, h, der), t)
def runge_kutta(x, y, t, h, t_final):
    while t < t_final: 
        x_new = x + (h/6) * (k1(x, y, t, der_x) + 2*k2(x, y, t, h, der_x) + 2*k3(x, y, t, h, der_x) + k4(x, y, t, h, der_x))
        y_new = y + (h/6) * (k1(x, y, t, der_y) + 2*k2(x, y, t, h, der_y) + 2*k3(x, y, t, h, der_y) + k4(x, y, t, h, der_y))
        x = x_new
        y = y_new
        t = t + h
    return x_new, y_new, t
    
t = 0 
y = 0
x = 0
t_final=10
h=0.001

print("Calling Heun's method")
print(heun(x, y, t, h, t_final))
print()
print()
print("Calling MidPoint's Method")
print(midpoint(x, y, t, h, t_final))
print()
print()
print("Calling Euler's Method")
print(euler(x, y, t, h, t_final))
print()
print()
print("Calling Raiston's Method")
print(raiston(x, y, t, h, t_final))
print()
print()
print("Calling Runge Kutta's Method")
print(runge_kutta(x, y, t, h, t_final))

