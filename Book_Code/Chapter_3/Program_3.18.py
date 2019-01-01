# Program 3.18: Program to Demonstrate Infinite while Loop and break

#n = 0
#while True:
#    print(f"The latest value of n is {n}")
#    n = n + 1

n = 0
while True:
    print(f"The latest value of n is {n}")
    n = n + 1
    if n > 5:
        print(f"The value of n is greater than 5")
        break

