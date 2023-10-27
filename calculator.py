import math # Importing math library for sqrt
def sqrt():
    sq = input("Do you want to square root a number? (yes/no): ") # Asking whether the user wants to sqrt a number
    while sq.lower()!="yes" and sq.lower()!="no":
        print("Please enter a valid choice ")
        sq = input("Do you want to square root a number? (yes/no): ")
    if sq.lower() == "yes": # Checking the input
        numsq = input("Enter the number you want to calculate the square root of: ")
        while not numsq.isdigit():
            print("Please enter a number ")
            numsq = input("Enter the number you want to calculate the square root of: ")
        print (f"The sqaure root of {numsq} is {'%.2f' % math.sqrt(int(numsq))}") # Priniting the sqrt of the provided number
        new_opt = input("Do you want to quit the square function? (yes/no): ")
        while new_opt.lower()!="yes" and new_opt.lower()!="no":
            print("Please enter a valid choice ")
            new_opt = input("Do you want to continue? (yes/no): ")
        if new_opt.lower() == "yes":
            new_opt2 = input("Do you want to quit the program? (yes/no): ")
            while new_opt2.lower()!="yes" and new_opt2.lower()!="no":
                print("Please enter a valid choice ")
                new_opt2 = input("Do you want to quit the program? (yes/no): ")
            if new_opt2.lower()=="yes":
                print("See you then!")
                exit()
            else:
                ...
        else:
            sqrt()

        

def main():
    sqrt()
    # Prompt user for the first number and validate the input
    print("Other operators like ('+', '-', '*', '/'', '%', '**') active")
    num1 = input("Enter a number: ")
    while not num1.isdigit():
        print("Please enter a number")  # Notify user of invalid input
        num1 = input("Enter a number: ")  # Retry input

    # Prompt user for the operation and validate the input
    oper = input("Enter any one operator ('+', '-', '*', '/'', '%', '**'): ")
    while oper not in ["+", "-", "*", "/", "%", "**", "sq"]:  
        print("Please enter a valid operator")  # Notify user of invalid operation
        oper = input("Enter any one operator ('+', '-', '*', '/'', '%', '**'): ")  # Retry input

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
    elif oper == "**":
        while int(num2) < 0 or int(num2) > 9:
            print("The value of the second number should be between 0 and 9")
            num2 = input("Enter another number: ")
        print("The answer is", int(num1) ** int(num2))  # Exponentiation
    else:
        print("This operation is not available for now")  # Notify user of unsupported operation
if __name__ == "__main__":
    main()