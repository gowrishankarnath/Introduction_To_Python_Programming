# Program 8.4: Program to Demonstrate the Return of Multiple Values from a Function


def return_multiple_items():
    monument = input("Which is your favorite monument? ")
    year = input("When was it constructed? ")
    return monument, year


def main():
    mnt, yr = return_multiple_items()
    print(f"My favorite monument is {mnt} and it was constructed in {yr}")

    result = return_multiple_items()
    print(f"My favorite monument is {result[0]} and it was constructed in {result[1]}")


if __name__ == "__main__":
    main()

