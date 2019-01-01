# Program 7.3: Write Python Program to Check for the Presence of a Key in the
# Dictionary and to Sum All Its Values

historical_events = {"apollo11": 1969, "great_depression": 1929, "american_revolution": 1775, "berlin_wall": 1989}


def check_key_presence():
    key = input("Enter the key to check for its presence ")
    if key in historical_events.keys():
        print(f"Key '{key}' is present in dictionary")
    else:
        print(f"Key '{key}' is not present in dictionary")


def sum_dictionary_values():
    print("Sum of all the values in the dictionary is")
    print(f"{sum(historical_events.values())}")


def main():
    check_key_presence()
    sum_dictionary_values()


if __name__ == "__main__":
    main()
