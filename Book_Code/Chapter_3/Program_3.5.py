# Program 3.5: Write a Program to Prompt for a Score between 0.0 and 1.0. If the
# Score Is Out of Range, Print an Error. If the Score Is between 0.0
# and 1.0, Print a Grade Using the Following Table
# Score   Grade
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
# < 0.6    F

score = float(input("Enter your score"))
if score < 0 or score > 1:
    print('Wrong Input')
elif score >= 0.9:
    print('Your Grade is "A" ')
elif score >= 0.8:
    print('Your Grade is "B" ')
elif score >= 0.7:
    print('Your Grade is "C" ')
elif score >= 0.6:
    print('Your Grade is "D" ')
else:
    print('Your Grade is "F" ')