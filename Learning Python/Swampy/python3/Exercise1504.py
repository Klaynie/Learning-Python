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

box = Rectangle()
box.corner = Point()
box.width = 200.0
box.height = 200.0
box.corner.x = 0
box.corner.y = 0
box.color = 'blue1'

box2 = Rectangle()
box2.corner = Point()
box2.width = 100.0
box2.height = 200.0
box2.corner.x = -100
box2.corner.y = -200
box2.color = 'green1'

point = Point()
point.x = 50
point.y = 50
point.color = 'red'

point2 = Point()
point2.x = -50
point2.y = -50
point2.color = 'yellow'

circle = Circle()
circle.center = Point()
circle.radius = 100
circle.center.x = 100
circle.center.y = 100
circle.color = 'snow'

draw_rectangle(canvas, box)
draw_rectangle(canvas, box2)
draw_point(canvas, point)
draw_point(canvas, point2)
draw_circle(canvas, circle)
world.mainloop()