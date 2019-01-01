# Program 5.4: Write Python Program to Count the Total Number of Vowels,
# Consonants and Blanks in a String


def main():
    user_string = input("Enter a string: ")
    vowels = 0
    consonants = 0
    blanks = 0
    for each_character in user_string:
        if(each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o'
                or each_character == 'u'):
            vowels += 1
        elif "a" < each_character < "z":
            consonants += 1
        elif each_character == " ":
            blanks += 1

    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")


if __name__ == "__main__":
    main()

