# Program 11.17: Program to Demonstrate the Use of super() Function


class Country:
    def __init__(self, country_name):
        self.country_name = country_name

    def country_details(self):
        print(f"Happiest Country in the world is {self.country_name}")


class HappiestCountry(Country):
    def __init__(self, country_name, continent):
        super().__init__(country_name)
        self.continent = continent

    def happy_country_details(self):
        print(f"Happiest Country in the world is {self.country_name} and is in {self.continent} ")


def main():
    finland = HappiestCountry("Finland", "Europe")
    finland.happy_country_details()


if __name__ == "__main__":
    main()

