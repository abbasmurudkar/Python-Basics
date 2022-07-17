import math
def circle_a(r):
    a = math.pi*(r**2)
    return a
def circle_c(r):
    x = 2*math.pi*r
    return x
r = 3
area = circle_a(r)
print("AREA = ", area)
circum = circle_c(r)
print("Circumference = ", circum)
