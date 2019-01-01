# Program 9.2: Program to Read and Print Each Line in "japan.txt" File Using
# with Statement. Sample Content of "japan.txt" File is Given Below.


def read_file():
    print("Printing each line in text file")
    with open("japan.txt") as file_handler:
        for each_line in file_handler:
            print(each_line.strip())


def main():
    read_file()


if __name__ == "__main__":
    main()


