# Program 9.15: Write Python program to write the data given below to a CSV file.
# Category,Winner,Film,Year
# Best Picture,Doug Mitchell and George Miller,Mad Max: Fury Road,2015
# Visual Effects,Richard Stammers,X-Men:Days of Future Past,2014
# Best Picture,Martin Scorsese and Leonardo DiCaprio,The Wolf of Wall Street,2013
# Music(Original Song),Adele Adkins and Paul Epworth,Skyfall from Skyfall,2012

import csv


def main():
    csv_header_name = ['Category', 'Winner', 'Film', 'Year']
    each_row = [['Best Picture', 'Doug Mitchell and George Miller', 'Mad Max: Fury Road', '2015'],
                ['Visual Effects', 'Richard Stammers', 'X - Men: Days of Future Past', '2014'],
                ['Best Picture', 'Martin Scorsese and Leonardo DiCaprio', 'The Wolf of Wall Street', '2013'],
                ['Music(Original Song)', 'Adele Adkins and Paul Epworth', 'Skyfall from Skyfall', '2012']]

    with open('oscars.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(csv_header_name)
        csv_writer.writerows(each_row)


if __name__ == "__main__":
    main()