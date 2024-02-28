import random

def dice_game():
    print("Welcome to the Dice Rolling Game!")
    print("I will roll a dice, and you have to guess if the next roll will be higher or lower.")
    
    current_roll = random.randint(1, 6)
    print("Current roll:", current_roll)
    
    while True:
        guess = input("Will the next roll be higher (h) or lower (l) than the current roll? (h/l): ").lower()
        
        next_roll = random.randint(1, 6)
        print("Next roll:", next_roll)
        
        if next_roll > current_roll and guess == 'h':
            print("You guessed correctly! Congratulations!")
        elif next_roll < current_roll and guess == 'l':
            print("You guessed correctly! Congratulations!")
        elif next_roll == current_roll:
            print("It's a tie! Roll again.")
        else:
            print("Sorry, you guessed incorrectly. Better luck next time!")
            
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        else:
            current_roll = next_roll

dice_game()
