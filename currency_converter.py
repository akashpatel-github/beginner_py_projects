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
    print(tabulate([["Key", "Currency"], ["C", "CAD"], ["P", "GBP"],
                        ["U", "USD"], ["I", "INR"], ["E", "Exit the program"]],
                    headers="firstrow", tablefmt="grid"))
    main()
    
def cad_converter():
    print("Convert from CAD to:")
    print(tabulate([["1", "USD"], ["2", "INR"], ["3", "GBP"]],
                     tablefmt="grid"))
    main()
def gbp_converter():
    print("Convert from GBP to:")
    print(tabulate([["1", "USD"], ["2", "INR"], ["3", "CAD"]],
                     tablefmt="grid"))
    main()
def usd_converter():
    print("Convert from USD to:")
    print(tabulate([["1", "INR"], ["2", "CAD"], ["3", "GBP"]],
                     tablefmt="grid"))
def inr_converter():
    print("Convert from INR to:")
    print(tabulate([["1", "USD"], ["2", "CAD"], ["3", "GBP"]],
                     tablefmt="grid"))
    main()
if __name__ == "__main__":
    main()