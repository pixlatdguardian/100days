import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇0
# Mapping the choices to their respective strings
choices = [rock, paper, scissors]
win_loss_map = {0: 2, 1: 0, 2: 1}

while True:
    player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))

    if player_choice < 0 or player_choice > 2:
        print("Invalid input. Please enter 0, 1, or 2.")
    else:
        computer_choice = random.randint(0, 2)
        print(f"You chose:\n{choices[player_choice]}")
        print(f"Computer chose:\n{choices[computer_choice]}")

        if player_choice == computer_choice:
            print("It's a draw!")
        elif win_loss_map[player_choice] == computer_choice:
            print("You win!")
        else:
            print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")