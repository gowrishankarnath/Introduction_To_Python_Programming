# Program 11.26: Write Python Program to Create a Class Called as Complex
# and Implement __add__() Method to Add Two Complex Numbers. Display
# the Result by Overloading the + Operator


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real} + i{self.imaginary}"


def main():
    complex_number_1 = Complex(4, 5)
    complex_number_2 = Complex(2, 3)
    complex_number_sum = complex_number_1 + complex_number_2
    print(f"Addition of two complex numbers {complex_number_1} and {complex_number_2} is {complex_number_sum}")


if __name__ == "__main__":
    main()

