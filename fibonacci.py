# Main function to handle user input and initiate Fibonacci series generation
def main():
    limit = input("Enter the upper limit of the series: ")  # Prompt user for the upper limit
    while not limit.isdigit():  # Validate input: Ensure the input is a digit
        print("Please enter a digit.")  # Prompt user for a valid input
        limit = input("Enter the upper limit of the series: ")  # Retry input
    print("Here is the Fibonacci Series till " + limit + ":")
    fibonacci(int(limit))  # Call the fibonacci function with the provided limit

# Function to generate and print Fibonacci series up to a given limit
def fibonacci(n: int):
    a, b = 0, 1  # Initialize the first two numbers of the Fibonacci series
    while b <= n:  # Loop until the next Fibonacci number is less than or equal to the limit
        series = b  # Store the current Fibonacci number in the 'series' variable
        b += a  # Calculate the next Fibonacci number by adding the previous two numbers
        a = series  # Update 'a' with the previous Fibonacci number (stored in 'series')
        if b <= n:  # Check if the next Fibonacci number is within the limit
            print(b)  # Print the Fibonacci number

# Check if the script is being run directly and call the main function
if __name__ == "__main__":
    main()  # Call the main function to start the program