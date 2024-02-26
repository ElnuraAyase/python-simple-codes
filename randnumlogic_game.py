import random 

def generate_random_number():
return random.randint(1, 100)


def guess_number():                                                # func for guessing logic
 random_number =generate_random_number()                           #generating rand num
 guessed =  False                                                  # variable is boolean = false for not guessed nums 

while not guessed:                                                 # start a while loop until guessed becomes"true"
 guess =  int(input(" Let's guess the number from (1,100).."))     # asking user for an number and converting to int
 if guess < random_number:                                         # checking if num is <
  print ("Lower than 0, try once again!")                          # informing 
  elif guess > random_number:                                      # another check
  print ("Higher than 100, give it another try!")                  # informing 2
 else:                                                             # if correct 
  print ("Wow! You guessed it right")                              # informing 3
   guessed = True                                                  # setting guess to true to exit the while  loop 


if __name__ == "__main__"                                          # pyhton check if the script is running directly not from the module, if yes then the name is set to the name of module 
guess_number ()                                                    # call the guess_number func to start the game
