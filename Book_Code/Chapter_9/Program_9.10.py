# Program 9.10: Write Python Program to Create a New Image from an Existing Image


def main():
    with open("rose.jpg", "rb") as existing_image, open("new_rose.jpg", "wb") as new_image:
        for each_line_bytes in existing_image:
            new_image.write(each_line_bytes)


if __name__ == "__main__":
    main()