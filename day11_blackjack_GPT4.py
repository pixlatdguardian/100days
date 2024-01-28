import random
# This is the results of working with GPT 4 to come up with an alternate solution.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_blackjack():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for Blackjack or user going over 21
        if user_score == 0 or user_score > 21:
            break

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_cards.append(deal_card())
        else:
            break

    # Dealer's turn: Dealer takes cards if score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Determine the game outcome
    if user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21 or user_score > computer_score:
        return "You win!"
    elif user_score < computer_score:
        return "You lose."
    elif user_score == computer_score:
        return "Draw!"

# Play the game
while True:
    print(play_blackjack())
    if input("Do you want to play another round of Blackjack? Type 'y' for yes, 'n' for no: ") != 'y':
        break
    print("\nNew Game!\n")

print("Thank you for playing Blackjack!")