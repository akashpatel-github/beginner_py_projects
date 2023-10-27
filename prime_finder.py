def main():# Define the main function to handle user input and display results
    # Keep running the loop until the user decides to exit
    while True:
        number = input("Enter a number (type 'exit' to quit): ")  # Prompt user for a number
        if number.lower() == "exit":  # Check if user wants to exit
            break  # Exit the loop and end the program
        while not number.isdigit():  # Check if input is a valid number
            print("Please enter a valid number.")  # Prompt user for a valid number
            number = input("Enter a number (type 'exit' to quit): ")  # Retry input
        real_no = int(number)  # Convert the input to an integer
        result = prime(real_no)  # Call the prime function to determine if the number is prime or composite
        print(result)  # Display the result to the user

# Function to check if a number is prime or composite
def prime(n):
    if n <= 1:
        return "It is neither prime nor composite number."  # Numbers less than or equal to 1 are neither prime nor composite
    for number in range(2, n):
        if n % number == 0:
            return "It is a composite number."  # If the number is divisible by any number between 2 and n-1, it is composite
    return "It is a prime number."  # If the number is not divisible by any number between 2 and n-1, it is prime

# Entry point of the program, check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program