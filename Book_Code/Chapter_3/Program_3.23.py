# Program 3.23: Write a Program Which Repeatedly Reads Numbers Until the User
# Enters 'done'. Once 'done' Is Entered, Print Out the Total, Count, and Average of the
# Numbers. If the User Enters Anything Other Than a Number, Detect Their Mistake
# Using try and except and Print an Error Message and Skip to the Next Number


total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        print(f"Sum of all the entered numbers is {total}")
        print(f"Count of total numbers entered {count}")
        print(f"Average is {total / count}")
        break
    else:
        try:
            total += float(num)
        except:
            print("Invalid input")
            continue
        count += 1