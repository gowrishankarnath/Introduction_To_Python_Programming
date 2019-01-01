# Program 3.9: Write a Program to Find the Average of n Natural Numbers
# Where n Is the Input from the User


number = int(input("Enter a number up to which you want to find the average"))
i = 0
sum = 0
count = 0
while i < number:
    i = i + 1
    sum = sum + i
    count = count + 1
average = sum/count
print(f"The average of {number} natural numbers is {average}")
