# Program 11.15: Program to Demonstrate Private Instance Variables in Python


class PrivateDemo:
    def __init__(self):
        self.nonprivateinstance = "I'm not private instance"
        self.__privateinstance = "I'm private instance"

    def display_privateinstance(self):
        print(f"{self.__privateinstance} used within method of a class")


def main():
    demo = PrivateDemo()
    print("Invoke Method having private instance")
    print(demo.display_privateinstance())
    print("Invoke non-private instance variable")
    print(demo.nonprivateinstance)
    print("Get attributes of object")
    print(demo.__dict__)
    print("Trying to access private instance variable outside the class results in error")
    print(demo.__privateinstance)


if __name__ == "__main__":
    main()




