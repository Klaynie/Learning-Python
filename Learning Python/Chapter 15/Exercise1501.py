import math

class Point(object):
    """Represents a point in 2-D space."""

def distance_between_points(point1, point2):
    return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

if __name__ == '__main__':
    point1 = Point()
    point1.x = 3
    point1.y = 3

    point2 = Point()
    point2.x = 4
    point2.y = 4

    print(distance_between_points(point1, point2))