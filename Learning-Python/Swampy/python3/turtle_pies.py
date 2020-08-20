import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    from mypolygon import *
    
def slice(t,h,alpha):
    r = h/(math.cos(math.radians(alpha/2)))
    l = 2*h*math.tan(math.radians(alpha/2))
    gamma = (180-alpha)/2
    fd(t, r)
    lt(t, 180-gamma)
    fd(t, l)
    lt(t, 180-gamma)
    fd(t, r)
    lt(t, 180-alpha)
    
def pie(t,h,n,theta):
    alpha = 360/n
    lt(t,theta)
    for i in range(n):
        slice(t,h,alpha)
        lt(t,360/n)
    
pie(bob,150,12,0)

wait_for_user()