# Program 3.6: Program to Display the Cost of Each Type of Fruit

fruit_type = input("Enter the Fruit Type:")
if fruit_type == "Oranges":
    print('Oranges are $0.65 a pound')
elif fruit_type == "Apples":
    print('Apples are $0.38 a pound')
elif fruit_type == "Bananas":
    print('Bananas are $0.42 a pound')
elif fruit_type == "Cherries":
    print('Cherries are $2.00 a pound')
else:
    print(f'Sorry, we are out of {fruit_type}')