# Prompt user for the first number and validate the input
num1 = input("Enter a number: ")
while not num1.isdigit():
    print("Please enter a number")  # Notify user of invalid input
    num1 = input("Enter a number: ")  # Retry input

# Prompt user for the operation and validate the input
oper = input("Enter the operation: ")
while oper not in ["+", "-", "*", "/", "%"]:
    print("Please enter a valid operation")  # Notify user of invalid operation
    oper = input("Enter the operation: ")  # Retry input

# Prompt user for the second number and validate the input
num2 = input("Enter another number: ")
while not num2.isdigit():
    print("Please enter a number")  # Notify user of invalid input
    num2 = input("Enter another number: ")  # Retry input

# Perform the specified operation and print the result
if oper == "+":
    print("The answer is", int(num1) + int(num2))  # Addition
elif oper == "-":
    print("The answer is", int(num1) - int(num2))  # Subtraction
elif oper == "*":
    print("The answer is", int(num1) * int(num2))  # Multiplication
elif oper == "/":
    print("The answer is", int(num1) / int(num2))  # Division
elif oper == "%":
    print("The answer is", int(num1) % int(num2))  # Modulus
else:
    print("This operation is not available for now")  # Notify user of unsupported operation