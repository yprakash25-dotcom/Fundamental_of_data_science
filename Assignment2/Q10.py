import random


def dice_guessing_game() -> None:
    print("Question 10: Dice Guessing Game")
    dice_value = random.randint(1, 6)
    guess_text = input("Guess the dice value (1 to 6): ").strip()
    if not guess_text.isdigit():
        print("Please enter a valid integer between 1 and 6.")
        return
    guess = int(guess_text)
    if guess < 1 or guess > 6:
        print("Guess must be between 1 and 6.")
        return

    print(f"Dice rolled: {dice_value}")
    if guess == dice_value:
        print("Result: Correct! 😊")
    elif abs(guess - dice_value) == 1:
        print("Result: Close guess. 😐")
    else:
        print("Result: Wrong guess. 😞")


if __name__ == "__main__":
    dice_guessing_game()
