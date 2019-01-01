# Program 4.2: Program to Find the Area of Trapezium Using the Formula
# Area = (1/2) * (a + b) * h Where a and b Are the 2 Bases
# of Trapezium and h Is the Height


def area_trapezium(a, b, h):
    area = 0.5 * (a + b) * h
    print(f"Area of a Trapezium is {area}")


def main():
    area_trapezium(10, 15, 20)


if __name__ == "__main__":
    main()

