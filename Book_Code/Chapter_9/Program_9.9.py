# Program 9.9: Write Python Program to Find the Longest Word in a File. Get the File
# Name from User. (Assume User Enters the File Name as "animals.txt" and its
# Sample Contents are as Below)


def read_file(file_name):
    with open(file_name) as file_handler:
        longest_word = ""
        for each_row in file_handler:
            word_list = each_row.rstrip().split()
            for each_word in word_list:
                if len(each_word) > len(longest_word):
                    longest_word = each_word
    print(f"The longest word in the file is {longest_word}")


def main():
    file_name = input("Enter file name: ")
    read_file(file_name)


if __name__ == "__main__":
    main()



