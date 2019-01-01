# Program 4.1: Program to Demonstrate a Function with and without Arguments


def function_definition_with_no_argument():
    print("This is a function definition with NO Argument")


def function_definition_with_one_argument(message):
    print(f"This is a function definition with {message}")


def main():
    function_definition_with_no_argument()
    function_definition_with_one_argument("One Argument")


if __name__ == "__main__":
    main()



