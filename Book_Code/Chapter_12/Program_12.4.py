# Program 12.4: Program to Get Text Response Content Using requests Module

import requests


def main():
    response_object = requests.get('https://www.gutenberg.org/cache/epub/419/pg419.txt')
    print("Text Contents")
    print(response_object.text)


if __name__ == "__main__":
    main()

