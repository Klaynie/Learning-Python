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
        if isinstance(other, Point):
            result.x = self.x + other.x
            result.y = self.y + other.y
        else:
            result.x = self.x + other[0]
            result.y = self.y + other[1]
        return result

    def __radd__(self, other):
        return self.__add__(other)

if __name__ == '__main__':
    point1 = Point(3,3)
    point2 = Point(2,2)
    tuple1 = (1,1)
    print(point1 + point2)
    print(point1 + tuple1)
    print(tuple1 + point1)