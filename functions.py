import random
import math

def f1(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
def f2(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def f3(x, y):
    result = random.gauss(0, 1) * math.sin(y)+ (x + y) * random.uniform(-1, 1)
    return result
def f4(x, y):
    result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1)
    return result
