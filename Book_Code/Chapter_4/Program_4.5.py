# Program 4.5. Calculate the value of sin(x) up to n terms using the series
# sin(x)=  x/1!-  x^3/3!+  x^5/5!-  x^7/7!+⋯  where x is in degrees


import math

degrees = int(input("Enter the degrees"))
nterms = int(input("Enter the number of terms"))
radians = degrees * math.pi / 180


def calculate_sin():
    result = 0
    numerator = radians
    denominator = 1
    for i in range(1, nterms+1):
        single_term = numerator / denominator
        result = result + single_term
        numerator = -numerator * radians * radians
        denominator = denominator * (2 * i) * (2 * i + 1)
    return result


def main():
    result = calculate_sin()
    print(f"value is sin(x) calculated using the series is {result} ")


if __name__ == "__main__":
    main()




