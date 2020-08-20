"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.000000001
 
def square(t, l):
    """
    Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location. t is a turtle.
    """
    for i in range(4):
        fd(t, l)
        lt(t)

def polygon(t, l, n):
    """
    Draws a polygon with n sides.
    
    t: Turtle
    n: number of sides
    l: length of each side.
    """
    for i in range(n):
        fd(t, l)
        lt(t, 360/n)

def polyline(t, n, length, angle):
    """
    Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t,r):
    """
    Draws a circle with radius r. t is a turtle.
    
    t: Turtle
    r: radius
    """
    arc(t,r,360)

def arc(t,r,angle):
    """
    Draws an arc with radius r over the given angle.
    
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    circumference = 2*math.pi*r
    arclength = circumference*angle/360
    n = int(circumference / 3) + 1
    step_length = arclength / n
    step_angle = angle/n
    polyline(t, n, step_length, step_angle)
    
def koch(t, length):
    if length<3:
        fd(t, length)
    else:
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)
        rt(t, 120)
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)

def snowflake(t, length, n):
    for i in range(n):
        koch(t, length)
        rt(t, 360/n)
        
def koch_line(t, length, n):
    if n == 1:
       fd(t, length)
    else:
       koch_line(t, length/3, n-1)
       lt(t, 60)
       koch_line(t, length/3, n-1)
       rt(t, 120)
       koch_line(t, length/3, n-1)
       lt(t, 60)
       koch_line(t, length/3, n-1)

def koch_snowflake(t, length, n):
    for i in range(3):
        koch_line(t, length, n)
        rt(t, 120)

if __name__ == '__main__':
    snowflake(bob, 100, 5)