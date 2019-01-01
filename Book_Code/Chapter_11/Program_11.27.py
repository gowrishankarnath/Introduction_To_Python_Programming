# Program 11.27: Consider a Rectangle Class and Create Two Rectangle Objects.
# This Program Should Check Whether the Area of the First Rectangle is Greater
# than Second by Overloading > Operator


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __gt__(self, other):
        rectangle_1_area = self.width * self.height
        rectangle_2_area = other.width * other.height
        return rectangle_1_area > rectangle_2_area


def main():
    rectangle_1_obj = Rectangle(5, 10)
    rectangle_2_obj = Rectangle(3, 4)
    if rectangle_1_obj > rectangle_2_obj:
        print("Rectangle 1 is greater than Rectangle 2")
    else:
        print("Rectangle 2 is greater than Rectangle 1")


if __name__ == "__main__":
    main()

