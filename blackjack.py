import random

# Represents a single playing card
class Card:
    # Suits and ranks used in a standard 52-card deck
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit  # e.g., "Hearts"
        self.rank = rank  # e.g., "K"

    # Determine the Blackjack value of the card
    def card_value(self):
        if self.rank.isdigit():  # For number cards: "2"–"10"
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K']:  # Face cards are worth 10
            return 10
        elif self.rank == 'A':  # Ace is worth 11 by default (can be 1 later)
            return 11

    # Return a tuple of suit, rank, and value
    def get_value(self):
        return (self.suit, self.rank, self.card_value())


# Represents a deck of 52 cards
class Deck:
    def __init__(self):
        # Create all combinations of suits and ranks
        self.total_cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    # Draw and remove a random card from the deck
    def draw_card(self):
        card = random.choice(self.total_cards)
        self.total_cards.remove(card)
        return card

    # Allow usage of len(deck) to get number of remaining cards
    def __len__(self):
        return len(self.total_cards)


# Calculate the total value of a hand, adjusting for Aces if needed
def hand_value(hand):
    value = sum(card.card_value() for card in hand)  # Add all card values
    aces = sum(card.rank == 'A' for card in hand)  # Count Aces

    # Convert Ace from 11 to 1 if total value exceeds 21
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


# The main Blackjack game application class
class BlackjackApp:
    def __init__(self):
        self.deck = Deck()  # Initialize a fresh deck
        # Deal two cards each to player and dealer
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]

    # Utility to format and display any hand
    def display_hand(self, hand, owner):
        return f"{owner}'s hand: {[(card.suit, card.rank) for card in hand]}, total value: {hand_value(hand)}"

    # Player's turn: can hit or stay
    def player_turn(self):
        while True:
            print(self.display_hand(self.player_hand, "Your"))
            action = input("Do you want to 'Hit' or 'Stay'? ").strip().lower()

            if action == 'hit':
                # Draw new card and show it
                new_card = self.deck.draw_card()
                self.player_hand.append(new_card)
                print(f"You drew: {new_card.suit} {new_card.rank} with value {new_card.card_value()}.")

                value = hand_value(self.player_hand)
                if value > 21:
                    # Busted if over 21
                    print(self.display_hand(self.player_hand, "Your"))
                    return "You busted! You lose."
                elif value == 21:
                    # Instant win if hits 21
                    return "Blackjack! You win!"

            elif action == 'stay':
                # End player's turn and let dealer play
                return self.dealer_turn()

            else:
                print("Invalid input. Please enter 'Hit' or 'Stay'.")

    # Dealer's turn: must draw until reaching at least 17
    def dealer_turn(self):
        print(self.display_hand(self.dealer_hand, "Dealer"))

        while hand_value(self.dealer_hand) < 17:
            # Dealer hits automatically until 17+
            new_card = self.deck.draw_card()
            self.dealer_hand.append(new_card)
            print(f"Dealer drew: {new_card.suit} {new_card.rank} with value {new_card.card_value()}.")

        dealer_value = hand_value(self.dealer_hand)
        player_value = hand_value(self.player_hand)

        # Final hands after dealer finishes
        print(self.display_hand(self.dealer_hand, "Dealer"))
        print(self.display_hand(self.player_hand, "Your"))

        # Compare values to determine the result
        if dealer_value > 21 or player_value > dealer_value:
            return "You win!"
        elif dealer_value > player_value:
            return "Dealer wins. You lose."
        else:
            return "It's a tie!"

    # Starts the game loop
    def start_game(self):
        print("🃏 Welcome to Blackjack!\n")
        result = self.player_turn()
        print("\n🎯 Game Over:", result)


# Run the game if this file is executed
if __name__ == "__main__":
    app = BlackjackApp()
    app.start_game()
