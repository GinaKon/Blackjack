import random    #yes

card_values = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_deck = card_values * 4


def card_value(card):
    if card.isdigit():
        return int(card)
    elif card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# def blackjack(card1, card2, card3, card4):
#     player_total = card_value(card1) + card_value(card2)
#     dealer_total = card_value(card3) + card_value(card4)

#     if player_total > 21:
#         return "Busted!"
#     elif player_total == 21:
#         return "Black Jack!"
#     elif player_total < dealer_total:
#         return "Hit me"
#     else:
#         return "I'll Stay"


def play_blackjack(playerhand, dealerhand):
    print(f"Your current hand: {playerhand}")
    action = input("Do you want to 'Hit' or 'Stay'? ").strip().lower()

    if action == 'hit':
        new_card = card_value(draw_card(card_deck))
        print(f"You drew a card with value {new_card}.")
        playerhand += new_card

        if playerhand > 21:
            return "You busted! You lose."
        elif playerhand == 21:
            return "Blackjack! You win!"
        else:
            return play_blackjack(playerhand, dealerhand)

    elif action == 'stay':
        print(f"Dealer's hand: {dealerhand}")
        print(f"Your final hand: {playerhand}")

        if dealerhand >= playerhand:
            return "Dealer wins. You lose."
        else:
            return "You win!"

    else:
        print("Invalid input. Please enter 'Hit' or 'Stay'.")
        return play_blackjack(playerhand, dealerhand)


playerhand = card_value(draw_card(card_deck)) + card_value(draw_card(card_deck))
dealerhand = card_value(draw_card(card_deck)) + card_value(draw_card(card_deck))
print(play_blackjack(playerhand, dealerhand))
# print(draw_card(card_deck))
print(card_deck)
