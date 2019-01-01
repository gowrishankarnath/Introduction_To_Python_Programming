# Program 6.4: Write Python Program to Sort Numbers in a List in Ascending Order
# Using Bubble Sort by Passing the List as an Argument to the Function Call


def bubble_sort(list_items):
    for i in range(len(list_items)):
        for j in range(len(list_items)-i-1):
            if list_items[j] > list_items[j+1]:
                temp = list_items[j]
                list_items[j] = list_items[j+1]
                list_items[j+1] = temp
    print(f"The sorted list using Bubble Sort is {list_items}")


def main():
    items_to_sort = [5, 4, 3, 2, 1]
    bubble_sort(items_to_sort)


if __name__ == "__main__":
    main()
