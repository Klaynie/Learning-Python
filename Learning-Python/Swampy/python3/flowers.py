import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    from mypolygon import *
    
def petal(t,d,l):
    h = d/2
    r = (4*h**2+l**2)/(8*h)
    angle = 2 * math.degrees(math.asin(l/(2*r)))
    gamma = (180-angle)/2
    arc(t,r,angle)
    lt(t,2*gamma)
    arc(t,r,angle)
    lt(t,2*gamma)
    
def flower(t,d,l,n):
    for i in range(n):
        petal(t,d,l)
        lt(t,360/n)
        
def tilted_flower(t,d,l,n,theta):
    lt(t,theta)
    flower(t,d,l,n)

tilted_flower(bob,25,100,32,0)

wait_for_user()