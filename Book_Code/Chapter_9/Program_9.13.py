# Program 9.13: Write Python program to read and display each row in
# "biostats.csv" CSV file. Sample content of "biostats.csv" is given below.

import csv


def main():
    with open('biostats.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        print("Print each row in CSV file")
        for each_row in csv_reader:
            #print(f'{",".join(each_row)}')
            print(",".join(each_row))


if __name__ == "__main__":
    main()