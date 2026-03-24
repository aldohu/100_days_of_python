cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art

playing = True
user_cards = []
pc_cards = []
import random

pc_sum = 0
user_sum = 0


def gameOver(user_cards, pc_cards):
    user_cards_sum = 0
    pc_cards_sum = 0
    for card in user_cards:
        user_cards_sum += card
    for card in pc_cards:
        pc_cards_sum += card

    # Game over conditions
    if user_cards_sum > 21:
        print("You Lost! You went over 21.")
        return False  # Game over
    elif user_cards_sum == 21:
        print("Blackjack! You Win!")
        return False  # Game over
    elif pc_cards_sum > 21:
        print("Computer went over 21! You Win!")
        return False  # Game over
    elif pc_cards_sum == 21:
        print("Computer has Blackjack! You Lost!")
        return False  # Game over
    elif user_cards_sum == pc_cards_sum:
        print("Draw!")
        return False  # Game over
    elif user_cards_sum < pc_cards_sum:
        print("You Lost! Computer has higher score.")
        print(f"Your cards are {user_cards} and your final score is {user_sum}")
        print(f"Computer's final score: {pc_sum}")
        return False  # Game over
    elif user_cards_sum > pc_cards_sum:
        print("You Win! You have higher score.")
        print(f"Your final score: {user_sum} and computer final score: {pc_sum}")
        return False  # Game over
    else:
        return True  # Game continues


# Initial deal
for i in range(2):
    user_cards.append(random.choice(cards))
    pc_cards.append(random.choice(cards))



# Calculate initial sums
for card in user_cards:
    user_sum += card
for card in pc_cards:
    pc_sum += card

new_game = input("Do you want to play game? (y/n)? ")
if new_game == "y":
    print(art.logo)
    playing = True  # Reset playing flag

    while playing:
        print(f"Your cards are {user_cards} and your current score is {user_sum}")
        print(f"CPU's first card is {pc_cards[0]}")

        user_new_card = input("Do you want to draw new card (y/n)? ")

        if user_new_card == "y":
            card_drawn = random.choice(cards)  # Fix: draw from cards list, not user_cards
            user_sum += card_drawn
            user_cards.append(card_drawn)

            # Check for bust immediately after drawing
            if user_sum > 21:
                print(f"You went over 21! Your final score: {user_sum}")
                print(f"Computer final score: {pc_sum}")
                playing = False  # End game
            # Check for blackjack
            elif user_sum == 21:
                print("Blackjack! Let's see the computer's cards...")
                # Show computer's full hand before game over
                print(f"Computer's cards: {pc_cards}, score: {pc_sum}")
                playing = gameOver(user_cards, pc_cards)
        else:
            # Player stands, game over
            playing = gameOver(user_cards, pc_cards)