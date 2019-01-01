# Program 9.14: Write Python program to read and display rows in "employees.csv" CSV file
# that start with employee name "Jerry". Sample content of "employees.csv" is given below

import csv


def main():
    with open('employees.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        print("Print rows in CSV file that start with employee name 'Jerry'")
        for each_row in csv_reader:
            if each_row[0] == "Jerry":
                print(",".join(each_row))


if __name__ == "__main__":
    main()