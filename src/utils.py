import math

def dot_product(a, b):
    return sum([x * y for x, y in zip(a, b)])

def norma(a):
    return math.sqrt(sum([x**2 for x in a]))