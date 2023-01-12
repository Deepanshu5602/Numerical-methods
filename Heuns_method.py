# Huen's Method
# y(i+1) = y(i) + (w1 + w2)*h*f(x,y) + w2*(h**2)*p1* df/dx + w2*q11*f(x,y) * df/dx 
# For Huen's Method 
# w1 + w2 = 1
# w2*p1 = w2*q11 = 0.5
#
# here df/dx is partial derivative wrt xi.

def f(t):
    return 4*(t**3) + 3*(t**2) + 2*t + 1
def der_f(t):
    return 12*(t**2) + 6*t + 2
yi = 0
h = 0.0001
b = 10
x = 0

while x <= b: 
    yi = yi + h*f(x) + 0.5*(h**2)*der_f(x) + 0.5*f(x)*(h**2)*der_f(x)
    x = x + h
print(yi)
print("percentage error: ", ((yi - 11110)/11110)*100)