# Import the random module to generate random choices
import random

# List of available options for the game
options = ['rock', 'paper', 'scissor']

# Function to handle the main game logic
def main():
    # Computer randomly selects an option from the list and converts it to lowercase
    comp = random.choice(options).lower()
    
    # Ask the user to input their choice and ensure it is a valid option
    while True:
        user_select = input("Rock, Paper, or Scissor? (type 'quit' to end the game): ")
    
        if user_select in options:
            break
        elif user_select == 'quit':
            print("Goodbye!")  # Print a goodbye message and exit if the user doesn't want to play anymore
            exit()
        else:
            print("Please select one of the options")
    # Print the computer's choice
    print(f"I choose {comp}.")

    # Determine the winner based on user and computer choices
    if user_select == comp:
        print("Oops! It's a draw.")
        play_again()  # Ask the user if they want to play again
    elif user_select == 'rock' and comp == 'scissor' or user_select == 'paper' and comp == 'rock' or user_select == "scissor" and comp == 'paper':
        print("Woohoo! You won the game.")
        play_again()  # Ask the user if they want to play again
    elif user_select == 'rock' and comp == 'paper' or user_select == 'paper' and comp == 'scissor' or user_select == "scissor" and comp == 'rock':
        print("Better luck next time!")
        play_again()  # Ask the user if they want to play again
    elif user_select == "quit":
        print("Goodbye!")  # Print a goodbye message and exit if the user doesn't want to play anymore
        exit()

# Function to ask the user if they want to play again
def play_again():
    again = input("Wanna play another round? ")
    if again == 'yes':
        main()  # Restart the game if the user wants to play again
    elif again == 'no':
        print("Goodbye!")  # Print a goodbye message and exit if the user doesn't want to play anymore
        exit()
    else:
        print("Please input either 'yes' or 'no'")  # Prompt the user to enter a valid response
        play_again()  # Ask the play_again() function again until a valid response is provided

# Check if the script is run as the main program
if __name__ == '__main__':
    main()  # Call the main function when the script is run