# Program 3.17: Write a Program to Find the Factorial of a Number


number = int(input('Enter a number'))
factorial = 1
if number < 0:
    print("Factorial doesn't exist for negative numbers")
elif number == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, number + 1):
        factorial = factorial * i
print(f"The factorial of number {number} is {factorial}")