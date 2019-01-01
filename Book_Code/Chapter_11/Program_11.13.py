# Program 11.13: Program to Demonstrate the Difference between Abstraction
# and Encapsulation


class foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

foo_object = foo(3,4)
foo_object.add()


