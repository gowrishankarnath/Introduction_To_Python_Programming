# Program 10.4 Write Python Program to Change the File Extension from .txt
# to .csv of All the Files (Including from Sub Directories) for a Given Path

import os
import glob


def rename_files_recursively(directory_path):
    print("File extension changed from .txt to .csv")

    for file_path in glob.glob(directory_path + '\**\*.txt', recursive=True):
        print(f"File with .txt extension {file_path} changed to", end="")
        try:
            pre, ext = os.path.splitext(file_path)
            print(f" File with .csv extension {pre + '.csv'}")
            os.rename(file_path, pre + '.csv')
        except Exception as e:
            print(e)


def main():
    directory_path = input('Enter the directory path from which you want to delete files recursively ')
    rename_files_recursively(directory_path)


if __name__ == "__main__":
    main()




#
# import os
#
#
# def rename_files_recursively(directory_path):
#     print("File extension changed from .txt to .csv")
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             print(f"File with .txt extension {file_path} changed to", end="")
#             try:
#                 pre, ext = os.path.splitext(file_path)
#                 print(f" File with .csv extension {pre + '.csv'}")
#                 os.rename(file_path, pre + '.csv')
#             except Exception as e:
#                 print(e)
#
#
# def main():
#     directory_path = input('Enter the directory path from which you want to delete files recursively ')
#     rename_files_recursively(directory_path)
#
#
# if __name__ == "__main__":
#     main()