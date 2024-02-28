import random

def word_guessing_game():
    # List of words to choose from
    words = ["apple", "banana", "orange", "grape", "strawberry", "pineapple", "watermelon"]
    
    # Choose a random word from the list
    secret_word = random.choice(words)
    
    # Initialize variables
    guessed_word = ['_'] * len(secret_word)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word.")
    print("The word has", len(secret_word), "letters.")
    
    while attempts < max_attempts:
        print(" ".join(guessed_word))  # Display the current state of the guessed word
        
        guess = input("Enter a letter or guess the whole word: ").lower()
        
        # Check if the guess is a single letter or the whole word
        if len(guess) == 1:
            if guess in secret_word:
                print("Correct guess!")
                # Update the guessed word with the correctly guessed letter(s)
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_word[i] = guess
            else:
                print("Incorrect guess! Try
