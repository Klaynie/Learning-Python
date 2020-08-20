import math
from math import sqrt

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    from mypolygon import *
    
bob.delay = 0.000000001
    
def fibonacci(t,n):
    if n >= 1:
        fib_prev_1_n = 1
        fib_prev_2_n = 0
        lt(t)
        for i in range(n-1):
            fib_n = fib_prev_1_n + fib_prev_2_n
            fib_prev_2_n = fib_prev_1_n
            fib_prev_1_n = fib_n
            arc(t,fib_n,90)

def not_archimedes(t,a,n):
    angle = 360*n
    for i in range(angle):
        r = a*(i+1)
        arc(t,r,i+1)
        print(i+1)

def archimedes(t,a,n):
    angle = 360*n
    for i in range(angle):
        length = a*i*1
        fd(t,length)
        lt(t,1)

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        lt(t, dtheta)
        theta += dtheta

archimedes(bob,0.0006,20)

wait_for_user()