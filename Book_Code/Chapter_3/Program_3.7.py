# Program 3.7: Program to Check If a Given Year Is a Leap Year

year = int(input('Enter a year'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a Leap Year')
        else:
            print(f'{year} is not a Leap Year')
    else:
        print(f'{year} is a Leap Year')
else:
    print(f'{year} is not a Leap Year')