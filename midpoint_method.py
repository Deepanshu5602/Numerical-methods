# mid point method 

#midpoint
def f(x):
    return (4*x*3)+(3*x*2)+(x*2)+(1)
yi = 0 
h = 0.1
b = 10
x = 0


while x<=b:
    yi = yi + h*f(x+h/2)
    x+=h
print(yi)
