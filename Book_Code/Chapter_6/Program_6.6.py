# Program 6.6: Input Five Integers (+ve and −ve). Find the Sum of Negative Numbers,
# Positive Numbers and Print Them. Also, Find the Average of All the Numbers
# and Numbers Above Average


def find_sum(list_items):
    positive_sum = 0
    negative_sum = 0
    for item in list_items:
        if item > 0:
            positive_sum = positive_sum + item
        else:
            negative_sum = negative_sum + item
    average = (positive_sum + negative_sum) / 5
    print(f"Sum of Positive numbers in list is {positive_sum}")
    print(f"Sum of Negative numbers in list is {negative_sum}")
    print(f"Average of item numbers in list is {average}")

    print("Items above average are")
    for item in list_items:
        if item > average:
            print(item)


def main():
    find_sum([-1, -2, -3, 4, 5])


if __name__ == "__main__":
    main()

