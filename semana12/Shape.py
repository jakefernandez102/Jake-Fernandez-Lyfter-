from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return f"{(2 * 3.14 * self.radius):.2f}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 4)

print(circle.calculate_area())
print(circle.calculate_perimeter())

print(square.calculate_area())
print(square.calculate_perimeter())

print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
