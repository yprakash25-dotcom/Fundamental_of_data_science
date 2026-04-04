# Q10_game.py  # File label for the guessing game

import random  # Import random for secret number generation

secret = random.randint(1, 50)  # Generate a secret number between 1 and 50
attempts = 7  # Limit the number of guesses

for i in range(attempts):  # Loop through each attempt
    guess = int(input("Guess the number (1-50): "))  # Read the user's guess

    if guess == secret:  # Check for a correct guess
        print("Correct! You win!")  # Display win message
        break  # Exit the loop on success
    elif guess > secret:  # Check if guess is too high
        print("Too high!")  # Give feedback
    else:
        print("Too low!")  # Give feedback
else:
    print("Better luck next time! The number was:", secret)  # Reveal secret if no win
