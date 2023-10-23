import sys

def main():
    number = input("Enter a number: ")
    while number.isalpha():
        print("Please enter a number")
        number = input("Enter a number: ")
    real_no = int(number)
    prime(real_no)

def prime(n:int):
    numbers = [3,4,5,6,7]
    for number in numbers:
        if n < 0:
            sys.exit("Please enter a positive number.")    
        elif n == 1 or n == 0:
            sys.exit("It is neither prime nor composite number.")
        elif n % number == 0 or n % 2 == 0:
            sys.exit("It is a composite number.") 
        else:
            sys.exit("It is a prime number.")

if __name__=="__main__":
    main()