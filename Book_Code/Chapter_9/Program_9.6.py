# Program 9.6: Consider "Sample_Program.py" Python file. Write Python program
# to remove the comment character from all the lines in a given Python source
# file. Sample content of "Sample_Program.py" Python file is given below


def main():
    with open("Sample_Program.py") as file_handler:
        for each_row in file_handler:
            each_row = each_row.replace("#", "")
            print(each_row, end="")
            # ind = each_row.find("#")
            # each_row = each_row.strip[each_row[ind]]
            # print(each_row)


if __name__ == "__main__":
    main()

