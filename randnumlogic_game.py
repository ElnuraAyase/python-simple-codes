import random 

def generate_random_number():
return random.randint(1, 100)

random_number = generate_random_number()

def guess_number():
 guessed =  False 

while not guessed:
 guess =  int(input(" Let's guess the number from (1,100)..")) 
 if guess < random_number:
  print ("Lower than 0, try once again!")
  elif guess > random_number: 
  print ("Higher than 100, give it another try!")\
 else:
  print ("Wow! You guessed it right")
   guessed = True

guess_number ()
