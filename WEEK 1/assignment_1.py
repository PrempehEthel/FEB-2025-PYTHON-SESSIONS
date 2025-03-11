# a simple Python program that asks the user to input two numbers and
# a mathematical operation (addition, subtraction, multiplication, or division)

# Inputs from the user
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Choosing which operation to perform
print("\nChoose the arithmetic operation you want")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Taking the user's input
choice = input("\nEnter option 1 or 2 or 3 or 4: ")

# Workspace
if choice == "1":
    add = num_1 + num_2
    addition = f"\nAnswer: {num_1} + {num_2} = {add}"
    print(addition)
elif choice == "2":
    sub = num_1 - num_2
    subtraction = f"\nAnswer: {num_1} - {num_2} = {sub}"
    print(subtraction)
elif choice == "3":
    mul = num_1 * num_2
    multiplication = f"\nAnswer: {num_1} * {num_2} = {mul}"
    print(multiplication)
elif choice == "4":
    if num_2 != 0:
        div = num_1 / num_2
        division = f"\nAnswer: {num_1} / {num_2} = {div}"
        print(division)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("\nInvalid choice! Please enter a valid option (1,2,3,4)")
