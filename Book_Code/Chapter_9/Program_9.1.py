# Program 9.1: Write Python Program to Read and Print Each Line in "egypt. txt" file.
# Sample Content of "egypt.txt" File is Given Below.


def read_file():
    file_handler = open("egypt.txt")
    print("Printing each line in text file")
    for each_line in file_handler:
        print(each_line)
    file_handler.close()


def main():
    read_file()


if __name__ == "__main__":
    main()
