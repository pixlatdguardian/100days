### This was a fun challenge, I wrote it all by myself, then used chatGPT to clean it 
### up and add error and input checking.
import random
logo="""
   ___      _      _                  _  __                                
  / __|__ _| |_ __| |_    _ __  ___  (_)/ _|  _  _ ___ _  _   __ __ _ _ _  
 | (__/ _` |  _/ _| ' \  | '  \/ -_) | |  _| | || / _ \ || | / _/ _` | ' \ 
  \___\__,_|\__\__|_||_| |_|_|_\___| |_|_|    \_, \___/\_,_| \__\__,_|_||_|
                                              |__/                         
"""

print(logo)

def guess_number(number):
  while True:
      try:
          guess = int(input("Make a guess:\n"))
          if 1 <= guess <= 100:
              if guess > number:
                  print("Too High.")
              elif guess < number:
                  print("Too Low.")
              else:
                  print(f"You got the number correct! the number was {number}")
              return guess
          else:
              print("Please enter a number between 1 and 100.")
      except ValueError:
          print("Invalid input. Please enter a number.")

    
def game():
  number = random.randint(1,100)
  #print(number)
  
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  
  while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == "easy":
      guesses = 10
      print(f"You have {guesses} guesses left.")
      break
    elif difficulty == "hard":
      guesses = 5
      print(f"You have {guesses} guesses left.")
      break
    else:
      print("Type 'easy' or 'hard'")
      
  
  while True:
    guess = guess_number(number)
    guesses -= 1
    
    if  number == guess:
      print("You Won!")
      break
    elif number != guess and guesses < 1:
      print(f"Sorry, game over. The correct number was {number}")
      break
    print(f"You have {guesses} guesses left.")

while True:
  game()
  play = input("Want to play? Input 'y' for yes, 'n' for no:\n")
  if play == "n":
    break