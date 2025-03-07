import random

print(
    "Welcome to the game! This is a number guessing game.\n"
    "You have 5 attempts to guess the number between 50 and 100. Let's start the game!"
)

# Generate a random number between 50 and 100
number_to_guess = random.randrange(50, 100)

chances = 5
guess_counter = 0

# Main game loop
while guess_counter < chances:

    guess_counter += 1
    try:
        my_guess = int(input(f"Attempt {guess_counter}/{chances} - Please enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the guess is correct
    if my_guess == number_to_guess:
        print(
            f"🎉 Congratulations! The number is {number_to_guess}, and you found it right in {guess_counter} attempts!"
        )
        break

    # Check if guess is too high or too low
    elif my_guess > number_to_guess:
        print("📈 Your guess is too high, try again!")
    else:
        print("📉 Your guess is too low, try again!")

# If all chances are used and the number is not guessed
if my_guess != number_to_guess:
    print(f"😢 Oops, sorry! The number was {number_to_guess}. Better luck next time!")
