# Program 7.6: Write Python Program to Count the Number of Characters in a String
# Using Dictionaries. Display the Keys and Their Values in Alphabetical Order


def construct_character_dict(word):
    character_count_dict = dict()
    for each_character in word:
        character_count_dict[each_character] = character_count_dict.get(each_character, 0) + 1

    sorted_list_keys = sorted(character_count_dict.keys())
    for each_key in sorted_list_keys:
        print(each_key, character_count_dict.get(each_key))


def main():
    word = input("Enter a string ")
    construct_character_dict(word)


if __name__ == "__main__":
    main()

