# Program 11.21: Program to Demonstrate the Construction of Method
# Resolution Order in Python


class First:
    def my_method(self):
        print("You found in Class First")

class Second:
    def my_method(self):
        print("You found in Class Second")

class Third:
    def my_method(self):
        print("You found in Class Third")

class Fourth(Third, First):
    pass

class Fifth(Third, Second):
    pass

class Sixth(Fifth, Fourth):
    pass


def main():
    obj = Sixth()
    obj.my_method()
    print(Sixth.mro())


if __name__ == "__main__":
    main()


