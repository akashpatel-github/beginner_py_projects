num1 = input("Enter a number: ")
while not num1.isdigit():
    print("Please enter a number")
    num1 = input("Enter a number: ")

oper = input("Enter the operation: ")
while oper not in ["+", "-", "*", "/", "%"]:
    print("Please enter a valid operation")
    oper = input("Enter the operation: ")
num2 = input("Enter a number: ")
while not num2.isdigit():
    print("Please enter a number")
    num2 = input("Enter a number: ")
if oper == "+":
    print("The answer is", int(num1) + int(num2))
elif oper == "-":
    print("The answer is", int(num1) - int(num2))
elif oper == "*":
    print("The answer is", int(num1) * int(num2))
elif oper == "/":
    print("The answer is", int(num1) / int(num2))
elif oper == "%":
    print("The answer is", int(num1) % int(num2))
else:
    print("This operation is not available for now")
