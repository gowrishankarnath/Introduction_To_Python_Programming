# Program 11.12: Program to Illustrate Class Variables and Instance Variables


class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.dog_name = name


d = Dog('Fido')
e = Dog('Buddy')

print(f"Value for Shared Variable or Class Variable 'kind' is '{d.kind}'")
print(f"Value for Shared Variable or Class Variable 'kind' is '{e.kind}'")
print(f"Value for Unique Variable or Instance Variable 'dog_name' is '{d.dog_name}'")
print(f"Value for Unique Variable or Instance Variable 'dog_name' is '{e.dog_name}'")