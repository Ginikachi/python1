## No 5:

class Point:
    """ A point on a line segment. """

    def __init__(self, x, y):
        """ (Point, number, number) -> NoneType

        A new Point at position (x, y) on a line segment.

        >>> p = Point(1, 3)
        >>> p.x
        1
        >>> p.y
        3
        """

        self.x = x
        self.y = y

class LineSegment:
    """ A line segment. """

    def __init__(self, point1, point2):
        """ (LineSegment, point, point) -> NoneType

        A new LineSegment connecting point1 to point2.

        >>> p1 = Point(1, 3)
        >>> p2 = Point(4, 9)
        >>> segment = LineSegment(p1, p2)
        >>> segment.startpoint == p1
        True
        >>> segment.endpoint == p2
        True
        >>> p1.x
        1
        >>>segment.startpoint.x
        1
        >>> p2.x
        4
        >>> segment.endpoint.x
        4
        """

        self.startpoint = point1
        self.endpoint = point2

## NB: self.startpoint is used. It must not always be self.'the variable' e.g
## self.point1; you can use self.'anything' as long as you equate it the
## variable that has been initialized in def __init__. E.g,
## self.startpoint = point1.

    def slope(self):
        """ (LineSegment) -> number

        Return the slope of the given line segment.

        >>> segment = LineSegment(Point(1, 3), Point(4, 9))
        >>> segment.slope()
        2.0
        """

        slope = (segment.endpoint.y - segment.startpoint.y) /(
            segment.endpoint.x - segment.startpoint.x)

        return slope

        
    def length(self):
        """ (LineSegment) -> number

        Return the length of the given line segment.
        >>> segment = LineSegment(Point(1, 3), Point(4, 9))
        >>> segment.length()
        6.708203932499369
        """

        import math
        
        x_length = segment.endpoint.x - segment.startpoint.x
        y_length = segment.endpoint.y - segment.startpoint.y

        Line_length = math.sqrt((x_length**2) + (y_length**2))

        return Line_length

       



        
        
        
