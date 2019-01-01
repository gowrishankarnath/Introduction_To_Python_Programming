# Program 8.8: Write a Function Which Receives a Variable Number of
# Strings as Arguments. Find Unique Characters in Each String


def find_unique(*all_words):
    for each_word in all_words:
        unique_character_list = list(set(each_word))
        print(f"Unique characters in the word {each_word} are {unique_character_list}")


def main():
    find_unique("egg", "immune", "feed", "vacuum", "goddessship")


if __name__ == "__main__":
    main()

