# Program 4.11: Program to Demonstrate the Use of *args and **kwargs


def cheese_shop(kind, *args, **kwargs):
    print(f"Do you have any {kind} ?")
    print(f"I'm sorry, we're all out of {kind}")
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])


def main():
    cheese_shop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shop_keeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")


if __name__ == "__main__":
    main()