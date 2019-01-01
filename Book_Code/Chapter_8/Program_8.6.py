# Program 8.6: Write Pythonic Code to Sort a Sequence of Names according
# to Their Alphabetical Order Without Using sort() Function


def read_list_items():
    print("Enter names separated by a space")
    list_items = input().split()
    return list_items


def sort_item_list(items_in_list):
    n = len(items_in_list)
    for i in range(n):
        for j in range(1, n-i):
            if items_in_list[j-1] > items_in_list[j]:
                (items_in_list[j-1], items_in_list[j]) = (items_in_list[j], items_in_list[j-1])
    print("After Sorting")
    print(items_in_list)


def main():
    all_items = read_list_items()
    sort_item_list(all_items)


if __name__ == "__main__":
    main()


