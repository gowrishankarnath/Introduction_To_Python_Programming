# Program 3.22: Program to Check for ZeroDivisionError Exception

x = input("Enter value for x: ")
y = input("Enter value for y: ")
try:
    result = int(x) / int(y)
except ZeroDivisionError:
        print("Division by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Executing finally clause")
