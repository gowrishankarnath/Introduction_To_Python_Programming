# Program 11.25: Write Python Program to Calculate Area and Perimeter of
# Different Shapes Using Polymorphism

import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Area of Rectangle is {self.width * self.height}")

    def perimeter(self):
        print(f"Perimeter of Rectangle is {2 * (self.width + self.height)}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle is {math.pi * self.radius ** 2}")

    def perimeter(self):
        print(f"Perimeter of Circle is {2 * math.pi * self.radius}")


def shape_type(shape_obj):
    shape_obj.area()
    shape_obj.perimeter()


def main():
    rectangle_obj = Rectangle(10, 20)
    circle_obj = Circle(10)
    for each_obj in [rectangle_obj, circle_obj]:
        shape_type(each_obj)


if __name__ == "__main__":
    main()

