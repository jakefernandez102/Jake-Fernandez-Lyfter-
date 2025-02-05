class Circle:
    def __init__ (self,radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

circle1 = Circle(5)
print(circle1.getArea())

circle2 = Circle(10)
print(circle2.getArea())