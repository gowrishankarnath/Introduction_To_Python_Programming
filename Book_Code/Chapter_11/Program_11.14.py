# Program 11.14: Given a point(x, y), Write Python Program to Find Whether it
# Lies in the First, Second, Third or Fourth Quadrant of x - y Plane


class Quadrant:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def determine_quadrant(self):
        if self.x_coord > 0 and self.y_coord > 0:
            print(f"Point with coordinates {(self.x_coord, self.y_coord)} lies in the FIRST Quadrant")
        elif self.x_coord < 0 and self.y_coord < 0:
            print(f"Point with coordinates {(self.x_coord, self.y_coord)} lies in the THIRD Quadrant")
        elif self.x_coord > 0 and self.y_coord < 0:
            print(f"Point with coordinates {(self.x_coord, self.y_coord)} lies in the FOURTH Quadrant")
        elif self.x_coord < 0 and self.y_coord > 0:
            print(f"Point with coordinates {(self.x_coord, self.y_coord)} lies in the SECOND Quadrant")


def main():
    point = Quadrant(-1, 3)
    point.determine_quadrant()


if __name__ == "__main__":
    main()

