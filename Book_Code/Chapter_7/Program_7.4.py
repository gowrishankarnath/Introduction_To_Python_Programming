# Program 7.4: Write Python Program to Count the Number of Times an Item
# Appears in the List

novels = ["gone_girl", "davinci_code", "games_of_thrones", "gone_girl", "davinci_code"]


def main():
    count_items = dict()
    for book_name in novels:
        count_items[book_name] = count_items.get(book_name, 0) + 1

    print("Number of times a novel appears in list is")
    print(count_items)


if __name__ == "__main__":
    main()

