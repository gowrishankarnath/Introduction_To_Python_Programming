# Program 11.19: Program to Demonstrate Multiple Inheritance


class Poissonier:
    def __init__(self, poissonier_role):
        self.poissonier_role = poissonier_role

    def display_poissonier_chef_info(self):
        print(f"Chef is mainly involved in preparing {self.poissonier_role}")


class Entremetier:
    def __init__(self, entremetier_role):
        self.entremetier_role = entremetier_role

    def display_entremetier_chef_info(self):
        print(f"Chef is mainly involved in preparing {self.entremetier_role}")


class Cook(Poissonier, Entremetier):
    def __init__(self, poissonier_role, entremetier_role):
        Poissonier.__init__(self, poissonier_role)
        Entremetier.__init__(self, entremetier_role)

    def invoke_base_class_methods(self):
        Poissonier.display_poissonier_chef_info(self)
        Entremetier.display_entremetier_chef_info(self)


def main():
    print(f"Is Cook a derived class of Poissonier Base Class? {issubclass(Cook, (Entremetier, Poissonier))}")
    chef = Cook("SeaFood", "Vegetables")
    chef.invoke_base_class_methods()


if __name__ == "__main__":
    main()




