# Program 9.5: Consider the "rome.txt" File Specified in Program 9.3. Write
# Python Program to Read "rome.txt" File Using readlines() Method


def main():
    with open("rome.txt") as file_handler:
        print("Print file contents as a list")
        print(file_handler.readlines())


if __name__ == "__main__":
    main()
