import random

# Represents a single playing card
class Card:
    # Class attributes for suits and ranks of a standard deck
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit  # Suit of the card (e.g., Hearts)
        self.rank = rank  # Rank of the card (e.g., A, K, 10)

    # Returns the Blackjack value of the card
    def card_value(self):
        if self.rank.isdigit():  # Number cards (2-10)
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K']:  # Face cards (J, Q, K) are worth 10
            return 10
        elif self.rank == 'A':  # Ace can be worth 11 initially
            return 11

    # Returns a tuple with card info and its value
    def get_value(self):
        return (self.suit, self.rank, self.card_value())


# Represents a deck of 52 cards
class Deck:
    def __init__(self):
        # Create a full deck of 52 unique cards
        self.total_cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    # Draw a random card from the deck and remove it
    def draw_card(self):
        card = random.choice(self.total_cards)
        self.total_cards.remove(card)
        return card

    # Allow len() to be used to check remaining cards in the deck
    def __len__(self):
        return len(self.total_cards)


# Calculate the total value of a hand (adjusting Aces if necessary)
def hand_value(hand):
    value = sum(card.card_value() for card in hand)
    aces = sum(card.rank == 'A' for card in hand)  # Count number of Aces

    # If hand is over 21 and has Aces, reduce their value from 11 to 1
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


# Main function to simulate a round of Blackjack
def play_blackjack(player_hand, dealer_hand, deck):
    # Show player's current hand and total value
    print(f"Your current hand: {[(card.suit, card.rank) for card in player_hand]}, total value: {hand_value(player_hand)}")
    action = input("Do you want to 'Hit' or 'Stay'? ").strip().lower()

    # If player chooses to hit (draw another card)
    if action == 'hit':
        new_card = deck.draw_card()
        player_hand.append(new_card)
        print(f"You drew: {new_card.suit} {new_card.rank} with value {new_card.card_value()}.")

        # Check if player busted or hit Blackjack
        if hand_value(player_hand) > 21:
            return "You busted! You lose."
        elif hand_value(player_hand) == 21:
            return "Blackjack! You win!"
        else:
            # Recursively continue the game
            return play_blackjack(player_hand, dealer_hand, deck)

    # If player chooses to stay (end their turn)
    elif action == 'stay':
        print(f"Dealer's hand: {[(card.suit, card.rank) for card in dealer_hand]}, total value: {hand_value(dealer_hand)}")
        print(f"Your final hand: {[(card.suit, card.rank) for card in player_hand]}, total value: {hand_value(player_hand)}")

        # Dealer draws cards until reaching at least 17
        while hand_value(dealer_hand) < 17:
            new_card = deck.draw_card()
            dealer_hand.append(new_card)
            print(f"Dealer drew: {new_card.suit} {new_card.rank} with value {new_card.card_value()}.")

        dealer_value = hand_value(dealer_hand)
        player_value = hand_value(player_hand)

        print(f"Dealer's final hand: {[(card.suit, card.rank) for card in dealer_hand]}, total value: {dealer_value}")

        # Determine the winner based on final hand values
        if dealer_value > 21 or player_value > dealer_value:
            return "You win!"
        elif dealer_value > player_value:
            return "Dealer wins. You lose."
        else:
            return "It's a tie!"

    # If input is invalid, prompt again
    else:
        print("Invalid input. Please enter 'Hit' or 'Stay'.")
        return play_blackjack(player_hand, dealer_hand, deck)


# Initialize a new deck of cards
deck = Deck()

# Deal initial two cards to player and dealer
player_hand = [deck.draw_card(), deck.draw_card()]
dealer_hand = [deck.draw_card(), deck.draw_card()]

# Start the game
result = play_blackjack(player_hand, dealer_hand, deck)
print(result)