# Program 3.14: Demonstrate for Loop Using range() Function

print("Only ''stop'' argument value specified in range function")
for i in range(3):
    print(f"{i}")

print("Both ''start'' and ''stop'' argument values specified in range function")
for i in range(2, 5):
    print(f"{i}")

print("All three arguments ''start'', ''stop'' and ''step'' specified in range function")
for i in range(1, 6, 3):
    print(f"{i}")