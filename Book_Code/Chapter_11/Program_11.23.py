# Program 11.23: Program to Demonstrate the Use of super() Function in
# Multiple Inheritances


class First:
    def __init__(self):
        print("In First")
        super().__init__()



class Second:
    def __init__(self):
        print("In Second")
        super().__init__()



class Third(First, Second):
    def __init__(self):
        print("In Third")
        super().__init__()



def main():
    obj = Third()
    print(f"Method Resolution Order is {Third.mro()}")


if __name__ == "__main__":
    main()

