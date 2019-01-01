# Program 3.11: Write Python Program to Find the Sum of Digits in a Number


number = int(input('Enter a number'))

result = 0
remainder = 0

while number != 0:
    remainder = number % 10
    result = result + remainder
    number = int(number / 10)

print(f"The sum of all digits is {result}")


