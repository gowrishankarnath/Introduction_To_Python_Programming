# Program 11.22: Program to Demonstrate the Solving of Diamond Problem in Python


class First:
    def my_method(self):
        print("You found me in Class First")


class Second(First):
    pass


# class Third(First):
#     def my_method(self):
#         print("You found me in Class Third")
#         super().my_method()


class Third(First):
    def my_method(self):
        print("You found me in Class Third")


class Fourth(Second, Third):
    pass


def main():
    obj = Fourth()
    obj.my_method()
    print(f"Method Resolution Order is {Fourth.mro()}")


if __name__ == "__main__":
    main()





