import random

print("Welcome to the Number Guessing Game!")
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
