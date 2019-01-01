# Program 9.18: Consider the File Structure Given Below. Write Python Program
# to Delete All the Files and Subdirectories from the Extinct_Animals Directory

import os


def delete_files_recursively(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                print(f"{file_path} is deleted")
                os.remove(file_path)
            except Exception as e:
                print(e)


def main():
    directory_path = input('Enter the directory path from which you want to delete files recursively ')
    delete_files_recursively(directory_path)


if __name__ == "__main__":
    main()



