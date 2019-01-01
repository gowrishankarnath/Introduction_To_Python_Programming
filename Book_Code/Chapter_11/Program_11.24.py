# Program 11.24: Program to Demonstrate Polymorphism in Python


class Vehicle:
    def __init__(self, model):
        self.model = model

    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")


class Bike(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")


class Car(Vehicle):
    def vehicle_model(self):
        print(f"Vehicle Model name is {self.model}")


class Aeroplane:
    pass


def vehicle_info(vehicle_obj):
    vehicle_obj.vehicle_model()


def main():
    ducati = Bike("Ducati-Scrambler")
    beetle = Car("Volkswagon-Beetle")
    boeing = Aeroplane()

    for each_obj in [ducati, beetle, boeing]:
        try:
            vehicle_info(each_obj)
        except AttributeError:
            print("Expected method not present in the object")


if __name__ == "__main__":
    main()

