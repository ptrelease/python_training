class Point(object):

    count = 0 # only one of these

    @staticmethod
    def points():
        return Point.count

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def __str__(self):
        # .2f describes floating point format.
        # says ignore the int, and restrict to two decimal places
        # You can say something like 8.2f to limit the number of
        # characters before the decimal point
        return "Point at %.2f, %.2f" % (self.x, self.y)

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

class ColouredPoint(Point):

    colour = 'red'

    @staticmethod
    def get_colour():
        return ColouredPoint.colour

    def __init__(self, x, y):
        Point.__init__(self, x, y)

    def __str__(self):
        # .2f describes floating point format.
        # says ignore the int, and restrict to two decimal places
        # You can say something like 8.2f to limit the number of
        # characters before the decimal point
        return ColouredPoint.get_colour()



p1 = Point(1,2)
p2 = Point(3,4)

print(p1)
p2.move_by(5,6)
print(p2)
print(Point.points())

p3 = ColouredPoint(1,2)
print(p3)


