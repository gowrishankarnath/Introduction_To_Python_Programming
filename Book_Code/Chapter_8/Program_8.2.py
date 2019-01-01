# Program 8.2: Program to Populate Tuple with User-Entered Items

tuple_items = ()

total_items = int(input("Enter the total number of items: "))
for i in range(total_items):
    user_input = int(input("Enter a number: "))
    tuple_items += (user_input,)
print(f"Items added to tuple are {tuple_items}")


list_items = []
total_items = int(input("Enter the total number of items: "))
for i in range(total_items):
    item = input("Enter an item to add: ")
    list_items.append(item)

items_of_tuple = tuple(list_items)

print(f"Tuple items are {items_of_tuple}")

