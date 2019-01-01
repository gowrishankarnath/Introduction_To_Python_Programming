# Program 11.20: Program to Demonstrate Multiple Inheritance with
# Method Overriding


class Pet:
    def __init__(self, breed):
        self.breed = breed

    def about(self):
        print(f"This is {self.breed} breed")


class Insurable:
    def __init__(self, amount):
        self.amount = amount

    def about(self):
        print(f"Its insured for an amount of {self.amount}")


class Cat(Pet, Insurable):
    def __init__(self, weight, breed, amount):
        self.weight = weight
        Pet.__init__(self, breed)
        Insurable.__init__(self, amount)

    def get_weight(self):
        print(f"{self.breed} Cat weighs around {self.weight} pounds")


def main():
    cat_obj = Cat(15, "Ragdoll", "$100")
    cat_obj.about()
    cat_obj.get_weight()


if __name__ == "__main__":
    main()


