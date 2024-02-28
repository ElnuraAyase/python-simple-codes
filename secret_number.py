# Step 1: Define the secret number
secret_number = 7

# Step 2: Welcome the player and explain the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

# Step 3: Allow the player to guess the number
while True:
    # Step 4: Player enters their guess
    guess = int(input("Enter your guess (between 1 and 10): "))

    # Step 5: Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")
        break
    else:
        print("Sorry, that's not the number. Try again!")
