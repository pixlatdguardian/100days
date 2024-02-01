import random
import art
from game_data import data

def choose():
    a, b = random.sample(range(len(data)), 2)  # Ensures a and b are different
    return a, b

def compare(option_a, option_b, guess):
    if guess == "a":
        return data[option_a]['follower_count'] > data[option_b]['follower_count']
    else:  # Assuming guess is "b"
        return data[option_a]['follower_count'] < data[option_b]['follower_count']

def game():
    print(art.logo)
    score = 0
    option_a, option_b = choose()
    correct = True
    while correct:
        print(f"Compare A: {data[option_a]['name']}, a {data[option_a]['description']}, from {data[option_a]['country']}.")
        print(art.vs)
        print(f"Against B: {data[option_b]['name']}, a {data[option_b]['description']}, from {data[option_b]['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = compare(option_a, option_b, guess)
        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            option_a, option_b = option_b, random.randint(0, len(data)-1)  # Move B to A, choose new B
        else:
            print(f"Game over. Your score was: {score}.")
            break
game()
while input("Do you want to play? 'y' for yes, 'n' for no: ").lower() == 'y':
    game()
