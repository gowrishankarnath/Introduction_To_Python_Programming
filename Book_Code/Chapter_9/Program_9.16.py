# Program 9.16: Write Python Program to Read Data from ''pokemon.csv'' csv
# File Using DictReader. Sample Content of ''pokemon.csv'' is Given Below

import csv


def main():
    with open('pokemon.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{row['Pokemon']}, {row['Type']}")


if __name__ == "__main__":
    main()