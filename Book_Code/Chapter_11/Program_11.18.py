# Program 11.18: Program to Demonstrate the Overriding of the Base Class Method
# in the Derived Class


class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def book_info(self):
        print(f"{self.title} is authored by {self.author}")


class Fiction(Book):
    def __init__(self, author, title, publisher):
        super().__init__(author, title)
        self.publisher = publisher

    def book_info(self):
        print(f"{self.title} is authored by {self.author} and published by {self.publisher}")

    def invoke_base_class_method(self):
        super().book_info()


def main():
    print("Derived Class")
    silva_book = Fiction("Daniel Silva", "Prince of Fire", "Berkley")
    silva_book.book_info()
    silva_book.invoke_base_class_method()
    print("---------------------------------")
    print("Base Class")
    reacher_book = Book("Lee Child", "One Shot")
    reacher_book.book_info()


if __name__ == "__main__":
    main()


