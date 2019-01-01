# Program 3.19: Write a Program to Check Whether a Number Is Prime or Not


number = int(input('Enter a number > 1: '))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")