from tabulate import tabulate

# Define fixed exchange rates (as of today)
exchange_rates = {
    "USD": 1.0,
    "CAD": 1.39,  # Example exchange rate: 1 USD = 1.35 CAD
    "GBP": 0.83,  # Example exchange rate: 1 USD = 0.75 GBP
    "INR": 83.30,  # Example exchange rate: 1 USD = 74 INR
}

# Function to display the main menu and handle user input
def main():
    while True:
        default_view()  # Display the default view with available options
        print()
        opt = input("What do you want to convert? ")  # Prompt user for choice
        print()

        # Validate user input to ensure it is a letter
        while not opt.isalpha():
            print("Please enter the key next to the provided options.")
            print()
            opt = input("What do you want to do?: ")
            print()

        if opt.lower() == "c":
            currency_converter("CAD")  # Call CAD converter function
        elif opt.lower() == "p":
            currency_converter("GBP")  # Call GBP converter function
        elif opt.lower() == "u":
            currency_converter("USD")  # Call USD converter function
        elif opt.lower() == "i":
            currency_converter("INR")  # Call INR converter function
        elif opt.lower() == "e":
            print("Terminating the Currency Converter program. See you!")  # Exit the program
            print()
            break  # Exit the loop and end the program
        else:
            print("Please enter a valid key.")
            print()

# Function to display the default menu options
def default_view():
    print("Currency Converter is now active")
    print("")
    # Display options as a table
    print(tabulate([["Key", "Currency"], ["C", "CAD"], ["P", "GBP"],
                    ["U", "USD"], ["I", "INR"], ["E", "Exit the program"]],
                    headers="firstrow", tablefmt="grid"))

# Function for currency conversion
def currency_converter(from_currency):
    to_currency = input(f"Convert from {from_currency} to (USD/CAD/GBP/INR): ").upper()
    while to_currency not in exchange_rates:
        print("Enter a valid currency from the available options")
        to_currency = input(f"Convert from {from_currency} to (USD/CAD/GBP/INR): ").upper()
    
    amount = get_valid_amount(f"Please enter the amount in {from_currency} to be converted into {to_currency}: ")

    exchange_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * exchange_rate
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

# Function to validate the amount input
def get_valid_amount(prompt):
    while True:
        amount = input(prompt)
        if amount.isdigit():
            return int(amount)
        else:
            print("Enter a valid amount.")

# Check if the script is run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program