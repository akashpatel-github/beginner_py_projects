from random import randint, choice

# Main function to initiate the game
def main():
    # Ask the user what game they want to play
    choice = input("What do you want to play? Number guessing game (type 'num') or Word guessing game (type 'word')? ")

    # Validate the choice input
    while choice.lower() != 'num' and choice.lower() != 'word':
        print("Please type 'num' or 'word'")
        choice = input("What do you want to play? Number guessing game (type 'num') or Word guessing game (type 'word')? ")

    # Start the appropriate game based on the user's choice
    if choice.lower() == 'num':
        number_guess()
    elif choice.lower() == 'word':
        word_guess()

# Function to handle the number guessing game
def number_guess():
    # Ask the user for the upper limit and validate the input
    limit = input("Enter an upper limit: ")
    while not limit.isdigit():
        print("Please enter a number")
        limit = input("Enter an upper limit: ")
    while int(limit)<5:
        print("Please enter the upper limit to be 5 atleast")
        limit = input("Enter an upper limit: ")
    print("Guess a number between 0 and " + limit)

    # Generate a random number within the specified limit
    pick = randint(0, int(limit))
    count = 10
    # Continue looping until the user guesses the correct number or types 'e' to exit
    while count > 0:
        guess = input("Guess (type 'e' to exit): ")
        
        if guess.lower() == 'e':
            print("Goodbye!")
            return  # Exit the number_guess() function and return to main()

        # Validate the guess input
        if not guess.isdigit():
            print("Please enter a number")
            continue
        
        guess = int(guess)
        

        # Check if the guess is within the range
        if guess > int(limit) or guess < 0:
            print("Please enter a number within 0 and " + limit)
        elif guess == pick:
            print("You've guessed the right number!")
            play_again()
            exit()
        if count >1:
            if guess > pick:
                print("Please guess a smaller number.")
            elif guess < pick:
                print("Please guess a bigger number.")
        count-=1
        if count == 1:
            print("1 try left")
        elif count == 0:
            print("You've lost the game")
            print("The number was",pick) 
            play_again()
            exit()
        else:
            print(count,"tries left")
# Function to handle the word guessing game
def word_guess():
    words = ["python", "hangman", "programming", "computer", "developer", "pizza", "twitter", "java", "javascript", "html"]
    word_to_guess = choice(words)
    guessed_word = ['_'] * len(word_to_guess)
    guessed_letters = []
    count = 10
    while count>0:
        guess = input("Guess a letter or the whole word: ").lower()
 
        # Check if the input is a valid letter or a valid word
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've guessed this letter already.")
            else:
                guessed_letters.append(guess)
                if guess in word_to_guess:
                    print("Correct guess!")
                    # Update guessed_word with correctly guessed letter(s)
                    for i in range(len(word_to_guess)):
                        if word_to_guess[i] == guess:
                            guessed_word[i] = guess
                else:
                    print("Incorrect guess.")
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                print("Correct! You've guessed the word: " + word_to_guess)
                play_again()
                exit()
            else:
                print("Incorrect guess.")
        else:
            print("Invalid input. Please enter a single letter or a word of",len(word_to_guess),"letters.")
            continue

        print("Guessed word: " + " ".join(guessed_word))
        count-=1
        if count == 1:
            print("1 try left")
        elif count == 0:
            print("You've lost the game") 
            print("The word was: "+ word_to_guess)
            play_again()
            exit()
        else:
            print(count,"tries left")

# Function asking the user to play again
def play_again():            
    # Prompt the user asking to play again
    play_again = input("Do you want to play again? (yes/no): ")
    while play_again.lower() not in ['yes', 'no']:
        print("Please type either 'yes' or 'no'")
        play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        main()  # Call main() function again to restart the game
    else:
        print("Goodbye!")


# Check if the script is run directly and call the main function
if __name__ == "__main__":
    main()