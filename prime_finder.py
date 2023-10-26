import sys

def main():
    while True:
        number = input("Enter a number (type 'exit' to quit): ")
        if number.lower() == 'exit':
            break
        while not number.isdigit():
            print("Please enter a valid number.")
            number = input("Enter a number (type 'exit' to quit): ")
        real_no = int(number)
        result = prime(real_no)
        print(result)

def prime(n):
    if n <= 1:
        return "It is neither prime nor composite number."
    for number in range(2, n):
        if n % number == 0:
            return "It is a composite number."
    return "It is a prime number."

if __name__ == "__main__":
    main()