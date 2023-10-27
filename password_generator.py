import random
import string

# Main function to generate and display passwords
def main():
    # Ask user for the number of passwords to generate
    total = input("How many passwords do you want? ")
    
    # Validate input: Ensure the input is a number greater than or equal to 1
    while not total.isdigit() or int(total) < 1:
        print("Please enter a valid number greater than or equal to 1.")
        total = input("How many passwords do you want? ")

    # Ask user for the maximum length of the passwords
    length = input("Enter the maximum length of your password: ")
    
    # Validate input: Ensure the input is a number between 4 and 50
    while not length.isdigit() or int(length) < 4 or int(length) > 50:
        print("Password length should be between 4 and 50 characters.")
        length = input("Enter the maximum length of your password: ")

    # Generate and display the specified number of passwords
    for index in range(1, int(total) + 1):
        print(f"{index}. {generate_password(int(length))}")
        
# Generate a random password of a given length
def generate_password(length):
    # Define character sets for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly selecting characters from the defined sets
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Check if the script is being run directly and call the main function
if __name__ == "__main__":
    main()