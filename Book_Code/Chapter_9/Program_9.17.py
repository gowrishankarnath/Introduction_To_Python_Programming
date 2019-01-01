# Program 9.17: Write Python program to demonstrate the writing of data
# to a CSV file using DictWriter class

import csv


def main():
    with open('names.csv', 'w', newline='') as csvfile:
        field_names = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


if __name__ == "__main__":
    main()
