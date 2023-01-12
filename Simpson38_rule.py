# Simpsons 3/8
import numpy as np
a=0
n=11
n1=0
n2=10
h=(n2-n1)/(n-1)
x = np.linspace(n1, n2, n)
fx =  (-1, 2, 23, 86, 215, 434, 767, 1238, 1871, 2690, 3719)
# for i in range(n1,n2-2,3):
#     a+=(3*y[i+1]+y[i]+3*y[i+2]+y[i+3])*3*h/8
# if((n2)%3==1):
#     a+=(y[n2]+y[n2-1])*h/2
# elif((n2)%3==2):
#     a+=(4*y[n2-1]+y[n2-2]+y[n2])*h/3
res = fx[n1] + fx[n2]
i=0
while i< n:
    if i % 3!= 0:
      res = res + 2*fx[i]
    else:
      res = res + 3 * fx[i]
    i+= 1
res = res * ((3*h )/ 8)
print(res)