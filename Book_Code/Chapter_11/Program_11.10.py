# Program 11.10: Given the Coordinates (x, y) of a Center of a Circle and Its Radius,
# Write Python Program to Determine Whether the Point Lies Inside the Circle,
# On the Circle or Outside the Circle


class Circle:
    def __init__(self, radius=0, circle_x=0, circle_y=0, point_x=0, point_y=0):
        self.radius = radius
        self.circle_x_coord = circle_x
        self.circle_y_coord = circle_y
        self.point_x_coord = point_x
        self.point_y_coord = point_y
        self.status = ""

    def check_point_status(self):
        if (self.point_x_coord - self.circle_x_coord) ** 2 + (self.point_y_coord - self.circle_y_coord) ** 2 < self.radius ** 2:
            self.status = f"Point with coordinates {(self.point_x_coord, self.point_y_coord)} is inside the Circle"
        elif (self.point_x_coord - self.circle_x_coord) ** 2 + (self.point_y_coord - self.circle_y_coord) ** 2 > self.radius ** 2:
            self.status = f"Point with coordinates {(self.point_x_coord, self.point_y_coord)} is outside the Circle"
        else:
            self.status = f"Point with coordinates {(self.point_x_coord, self.point_y_coord)} is on the Circle"

        return self


def main():
    point = Circle(10, 2, 3, 9, 9)
    returned_object = point.check_point_status()
    print(returned_object.status)
    print(f"Is point an instance of Circle Class? {isinstance(point, Circle)}")
    print(f"Is returned_object an instance of Circle Class? {isinstance(returned_object, Circle)}")
    print(f"Identity of the location of point object is {id(point)}")
    print(f"Identity of the location of returned_object object is {id(returned_object)}")


if __name__ == "__main__":
    main()
