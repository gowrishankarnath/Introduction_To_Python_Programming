# Program 9.3: Write Python Program to Read "rome.txt" File Using
# read() Method. Sample Content of "rome.txt" File is Given Below


def main():
    with open("rome.txt") as file_handler:
        print("Print entire file contents")
        print(file_handler.read(), end="")
        #print(file_handler.read(13), end="")


if __name__ == "__main__":
    main()


