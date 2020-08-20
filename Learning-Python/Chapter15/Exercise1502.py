import math

class Point(object):
    """Represents a point in 2-D space."""

class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return rect

if __name__ == '__main__':
    box = Rectangle()
    box.corner = Point()
    box.width = 100.0
    box.height = 200.0
    box.corner.x = 0
    box.corner.y = 0

    print_point(box.corner)

    dx = 1
    dy = 1

    move_rectangle(box, dx, dy)
    print_point(box.corner)