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
    """Represents a point in 2-D space."""

class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner, color.
    """

def draw_rectangle(canvas, rect):
    bbox = [[-rect.width/2,-rect.height/2], [rect.width/2, rect.height/2]]
    canvas.rectangle(bbox, outline='black', width=2, fill= box.color)

world = World()
canvas = world.ca(width=500, height=500, background='white')

box = Rectangle()
box.corner = Point()
box.width = 100.0
box.height = 200.0
box.corner.x = 0
box.corner.y = 0
box.color = 'blue1'

draw_rectangle(canvas, box)
world.mainloop()