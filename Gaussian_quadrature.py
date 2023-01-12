def f(t):
    return 4*(t**3) - 3*(t**2) + 2*t - 1

# x is epsilon here.
def gauss_quadration(a, b , n):
    e, w = select_ew(n)
    x = []
    for i in range(len(w)):
        temp = (b - a) / 2 * e[i] + (b + a) / 2
        x.append(temp)
    area = 0
    for i in range(n):
        area = area + w[i] * f(x[i])
    area = area * (b - a) / 2
    return area

def select_ew(n):
    if n == 2:
        e = [-0.5773502691896257, 0.5773502691896257]
        w = [1, 1]
    elif n == 3:
        e = [-0.7745966692414834, 0, 0.7745966692414834]
        w = [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
    elif n == 4:
        e = [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526]
        w = [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538]
    elif n == 5:
        e = [-0.9061798459386640, -0.5384693101056831, 0, 0.5384693101056831, 0.9061798459386640]
        w = [0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891]
    return e, w

segments = 10
def segmentation(a, b, segments, n): 
    h = (b - a) / segments
    a_new = 0
    area = 0
    for i in range (segments):
        area = area + gauss_quadration(a_new, a_new + h, n)
        a_new = a_new + h
    return area

a = 0
b = 10
segments = 5
n = 2

print("Area with Segmentation {segments} and points {n} ".format(n = n, segments = segments), segmentation(a, b, segments, n))