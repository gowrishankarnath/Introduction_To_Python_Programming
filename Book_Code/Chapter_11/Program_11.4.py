# Program 11.4: Program to Illustrate the Creation of Multiple Objects for a Class


class Birds:

    def __init__(self, bird_name):
        self.bird_name = bird_name

    def flying_birds(self):
        print(f"{self.bird_name} flies above clouds")

    def non_flying_birds(self):
        print(f"{self.bird_name} is the national bird of Australia")


def main():
    vulture = Birds("Griffon Vulture")
    crane = Birds("Common Crane")
    emu = Birds("Emu")
    vulture.flying_birds()
    crane.flying_birds()
    emu.non_flying_birds()


if __name__ == "__main__":
    main()



