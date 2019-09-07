import math

def hypothenuse(a,b):
    cSquare = a**2 + b**2
    c = math.sqrt(cSquare)
    print('c is', c)
    return c

hypothenuse(3, 4)