# Program 4.12: Program to Demonstrate Command Line Arguments in Python

import sys


def main():
    print(f"sys.argv prints all the arguments at the command line including file name {sys.argv}")
    print(f"len(sys.argv) prints the total number of command line arguments including file name {len(sys.argv)}")
    print("You can use for loop to traverse through sys.argv")
    for arg in sys.argv:
        print(arg)


if __name__ == "__main__":
    main()

