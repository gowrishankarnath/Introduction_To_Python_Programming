# Program 6.8: Find Mean, Variance and Standard Deviation of List Numbers

import math


def statistics(list_items):
    mean = sum(list_items)/len(list_items)
    print(f"Mean is {mean}")
    variance = 0
    for item in list_items:
        variance += (item-mean)**2
    variance /= len(list_items)
    print(f"Variance is {variance}")
    standard_deviation = math.sqrt(variance)
    print(f"Standard Deviation is {standard_deviation}")


def main():
    statistics([1, 2, 3, 4])


if __name__ == "__main__":
    main()

