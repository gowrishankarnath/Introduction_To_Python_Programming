# Program 3.13: Program to Repeatedly Check for the Largest Number Until the
# User Enters "done"


largest_number = int(input("Enter the largest number initially"))
check_number = input("Enter a number to check whether it is largest or not")

while check_number != "done":
    if largest_number > int(check_number):
        print(f"Largest Number is {largest_number}")
    else:
        largest_number = int(check_number)
        print(f"Largest Number is {largest_number}")

    check_number = input("Enter a number to check whether it is largest or not")