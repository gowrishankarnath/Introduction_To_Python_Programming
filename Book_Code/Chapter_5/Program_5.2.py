# Program 5.2: Program to Demonstrate String Traversing Using the for Loop


def main():
    alphabet = "google"
    index = 0
    print(f"In the string '{alphabet}'")
    for each_character in alphabet:
        print(f"Character '{each_character}' has an index value of {index}")
        index += 1


if __name__ == "__main__":
    main()

