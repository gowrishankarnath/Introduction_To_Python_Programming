# Program 9.8: Write Python Program to Count the Occurrences of Each Word
# and Also Count the Number of Words in a "quotes.txt" File. Sample
# Content of "quotes.txt" File is Given Below


def main():
    occurrence_of_words = dict()
    total_words = 0
    with open("quotes.txt") as file_handler:
        for each_row in file_handler:
            words = each_row.rstrip().split()
            total_words += len(words)
            for each_word in words:
                occurrence_of_words[each_word] = occurrence_of_words.get(each_word, 0) + 1
        print("The number of times each word appears in a sentence is")
        print(occurrence_of_words)
        print(f"Total number of words in the file are {total_words}")


if __name__ == "__main__":
    main()
