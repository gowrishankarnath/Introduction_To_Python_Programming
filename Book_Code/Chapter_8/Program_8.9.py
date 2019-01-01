# Program 8.9: Write a Python Program That Accepts a Sentence as Input
# and Removes All Duplicate Words. Print the Sorted Words


def unique_words(user_input):
    words = user_input.split()
    print(f"The unique and sorted words are {sorted(list(set(words)))}")


def main():
    sentence = input("Enter a sentence ")
    unique_words(sentence)


if __name__ == "__main__":
    main()

