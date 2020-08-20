import math
from math import sqrt

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
    from swampy.World import World
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    from World import *

class Point(object):
    """Represents a point in 2-D space.
    attributes: x, y, color.
    """

class Circle(object):
    """"Represents a circle.
    attributes: center, radius, color.
    """

class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner, color.
    """

def draw_rectangle(canvas, rect):
    bbox = [[rect.corner.x,rect.corner.y], [rect.width + rect.corner.x, rect.height + rect.corner.y]]
    canvas.rectangle(bbox, outline='black', width=2, fill= rect.color)

def draw_point(canvas, point):
    canvas.circle([point.x,point.y], 1, outline='black', fill= point.color)

def draw_circle(canvas, circle):
    canvas.circle([circle.center.x,circle.center.y], circle.radius, outline= 'black', fill= circle.color)

world = World()
canvas = world.ca(width=500, height=500, background='white')

points = [[0,0], [0, 200], [150, 100]]
canvas.polygon(points, fill='blue')
points = [[0,0], [150, 100], [300,100], [300,0]]
canvas.polygon(points, fill='red')
bbox = [[0,0], [300,200]]
canvas.rectangle(bbox, outline='black', width=1, fill= None)
world.mainloop()