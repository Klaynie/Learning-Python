import math

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x = 0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __add__(self, other):
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

if __name__ == '__main__':
    point1 = Point(3,3)
    point2 = Point(2,2)

    print(point1 + point2)