# Program 9.4: Consider the "rome.txt" File Specified in Program 9.3. Write
# Python Program to Read "rome.txt" file Using readline() Method


def main():
    with open("rome.txt") as file_handler:
        print("Print a single line from the file")
        print(file_handler.readline(), end="")
        print("Print another single line from the file")
        print(file_handler.readline(), end="")


if __name__ == "__main__":
    main()


