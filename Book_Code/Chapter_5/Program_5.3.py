# Program 5.3: Program to Print the Characters Which Are Common in Two Strings


def common_characters(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")


def main():
    common_characters('rose', 'goose')


if __name__ == "__main__":
    main()
