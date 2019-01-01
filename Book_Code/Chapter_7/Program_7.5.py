# Program 7.5: Write Python Program to Count the Number of Times Each Word
# Appears in a Sentence


def main():
    count_words = dict()
    sentence = input("Enter a sentence ")
    words = sentence.split()

    for each_word in words:
        count_words[each_word] = count_words.get(each_word, 0) + 1
    print("The number of times each word appears in a sentence is")
    print(count_words)


if __name__ == "__main__":
    main()

