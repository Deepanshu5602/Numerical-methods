import numpy as np

a = 0
b = 10

n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f =  (-1, 2, 23, 86, 215, 434, 767, 1238, 1871, 2690, 3719)

I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])

print(I_trap)