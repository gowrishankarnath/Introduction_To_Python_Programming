# Program 6.5: Write Python Program to Conduct a Linear Search for a Given Key
# Number in the List and Report Success or Failure


def read_key_item():
    key_item = int(input("Enter the key item to search: "))
    return key_item


def linear_search(search_key):
    list_of_items = [10, 20, 30, 40, 50]
    found = False
    for item_index in range(len(list_of_items)):
        if list_of_items[item_index] == search_key:
            found = True
            break

    if found:
        print(f"{search_key} found at position {item_index + 1}")
    else:
        print("Item not found in the list")


def main():
    key_in_list = read_key_item()
    linear_search(key_in_list)


if __name__ == "__main__":
    main()