from tabulate import tabulate  # Import the tabulate module for formatting data as tables
import textwrap  # Import textwrap module for wrapping text to fit within specified width
# main function
def main():
    default_view()
    print("")
    opt = input("What do you want to convert? ")
    print("")
    while not opt.isalpha():
        print("Please enter the key next to the provided options. ")  # Ensure valid input
        print(" ")
          # Display options again
        opt = input("What do you want to do?: ")  # Prompt user for choice again

    if opt.lower() == "c":
        cad_converter()
    elif opt.lower() == "p":
        gbp_converter()
    elif opt.lower() == "u":
        usd_converter()
    elif opt.lower() == "i":
        inr_converter()
    elif opt.lower() == "e":
        print("Terminating the Currency Converter program. See you!")  # Exit the program
        print(" ")
        exit()
    else:
        print(" ")
        print("Please enter a valid key.")
def default_view():
    print("")
    print("Currency Converter")
    print("")
    # Display options as a table
    print(tabulate([["Key", "Currency"], ["C", "CAD to: "], ["P", "GBP to: "],
                        ["U", "USD to: "], ["I", "INR to: "], ["E", "Exit"]],
                    headers="firstrow", tablefmt="grid"))
    
def cad_converter():
    ...
def gbp_converter():
    ...
def usd_converter():
    ...
def inr_converter():
    ...
if __name__ == "__main__":
    main()