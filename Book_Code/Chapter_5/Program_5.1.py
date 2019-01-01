# Program 5.1: Write Python Code to Determine Whether the Given String
# Is a Palindrome or Not Using Slicing


def main():
    user_string = input("Enter string: ")
    if user_string == user_string[::-1]:
        print(f"User entered string is palindrome")
    else:
        print(f"User entered string is not a palindrome")


if __name__ == "__main__":
    main()

