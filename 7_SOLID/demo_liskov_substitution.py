class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width ** 2


def print_area(rectangle):
    print(rectangle.area())


r = Rectangle(2, 3)
s = Square(2)

print_area(r)  # 6
print_area(s)  # 4



