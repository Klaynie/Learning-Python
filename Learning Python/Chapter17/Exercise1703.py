import math

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x = 0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

if __name__ == '__main__':
    point = Point(3,3)

    print(point)