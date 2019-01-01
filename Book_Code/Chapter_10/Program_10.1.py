# Program 10.1: Given an Input File Which Contains a List of Names and
# Phone Numbers Separated by Spaces in the Following Format:
# Alex 80-23425525
# Emily 322-56775342
# Grace 20-24564555
# Anna 194-49611659
# Phone Number Contains a 3- or 2-Digit Area Code and a Hyphen Followed By an
# 8-Digit Number.
# Find All Names Having Phone Numbers with a 3-Digit Area Code Using Regular
# Expressions.


import re


def main():
    pattern = re.compile(r"(\w+)\s+\d{3}-\d{8}")
    with open("person_details.txt", "r") as file_handler:
        print("Names having phone numbers with 3 digit area code")
        for each_line in file_handler:
            match_object = pattern.search(each_line)
            if match_object:
                print(match_object.group(1))


if __name__ == "__main__":
    main()

