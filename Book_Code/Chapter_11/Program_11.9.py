# Program 11.9: Given Three Points (x1, y1), (x2, y2) and (x3, y3), Write a Python
# Program to Check If they are Collinear


class Collinear:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def check_for_collinear(self, point_2_obj, point_3_obj):

        if (point_3_obj.y_coord - point_2_obj.y_coord)*(point_2_obj.x_coord - self.x_coord) == \
                (point_2_obj.y_coord - self.y_coord)*(point_3_obj.x_coord - point_2_obj.x_coord):

            print("Points are Collinear")
        else:
            print("Points are not Collinear")


def main():
    point_1 = Collinear(1, 1)
    point_2 = Collinear(1, 4)
    point_3 = Collinear(1, 5)
    point_1.check_for_collinear(point_2, point_3)


if __name__ == "__main__":
    main()


