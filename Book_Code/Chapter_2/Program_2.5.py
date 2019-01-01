# Program 2.5: Write Python Program to Convert the Given Number of Days
# to a Measure of Time Given in Years, Weeks and Days. For Example,
# 375 Days Is Equal to 1 Year, 1 Week and 3 Days (Ignore Leap Year).

number_of_days = int(input("Enter number of days"))
number_0f_years = int(number_of_days/365)
number_of_weeks = int(number_of_days % 365 / 7)
remaining_number_of_days = int(number_of_days % 365 % 7)
print(f"Years = {number_0f_years}, Weeks = {number_of_weeks}, Days = {remaining_number_of_days}")
