# Program 9.7: Write Python Program to Reverse Each Word in "secret_societies.txt" file.
# Sample Content of "secret_societies.txt" is Given Below


def main():
    reversed_word_list = []
    with open("secret_societies.txt") as file_handler:
        for each_row in file_handler:
            word_list = each_row.rstrip().split(" ")
            for each_word in word_list:
                reversed_word_list.append(each_word[::-1])
            print(" ".join(reversed_word_list))
            reversed_word_list.clear()


if __name__ == "__main__":
    main()


