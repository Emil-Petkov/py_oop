from math import pi


class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.width * self.length


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return pi * self.r ** 2


square = Square(2)
rectangle = Rectangle(4, 7)
circle = Circle(5)

square_area = square.calculate_area()
print(square_area)  # 4
print()
rectangle_area = rectangle.calculate_area()
print(rectangle_area)  # 28
print()
circle_area = circle.calculate_area()
print(circle_area)  # 78.53981633974483
