def display_word(word, guessed_letters):
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter
      else :
      display += "-"
    return display
  def main ():
    print = ("Welcome to the "Simple Guess" English game! ")
    word_to_guess = input("Enter the word you want to guess later").lower()
    guessed_letters = []
    attempts = 5 
  
while True:
  print( "\nWord to guess: ", display_word(word_to_guess, guessed_letters))
