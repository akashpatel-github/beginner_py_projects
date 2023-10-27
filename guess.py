from random import randint

# Ask user to input an upper limit, ensuring it's a valid number
limit = input("Enter an upper limit: ")
while not limit.isdigit():
    print("Please enter a number")
    limit = input("Enter an upper limit: ")

# Generate a random number within the specified limit
pick = randint(0, int(limit))

# Ask user to guess the number, ensuring it's a valid number
guess = input("Guess the number: ")
while not guess.isdigit():
    print("Please enter a number")
    guess = input("Guess the number ")

# Check if the initial guess is within the range
if int(guess) > int(limit) or int(guess) < 0:
    print("Please enter a number within the range.")

# Continue asking for guesses until the correct number is guessed
while int(guess) != pick:
    if int(guess) > pick:
        print("Please guess a smaller number.")
    elif int(guess) < pick:
        print("Please guess a bigger number.")

    guess = int(input("Guess the random number: "))

# Print a success message when the correct number is guessed
print("You've guessed the right number!")
