import random    

class Card:

    def __init__(self, suit, rank):
     self.suit = suit
     self.rank = rank
      
      
    def card_value(self):
     if self.rank.isdigit():
         return int(self.rank)
     elif self.rank in ['J', 'Q', 'K']:
         return 10
     elif self.rank == 'A':
         return 11
     
    
    def get_value(self):
       return (self.suit, self.card_value())


class Deck:

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


    def __init__(self):
        self.total_cards = []
        for i in Deck.suits:
           for x in Deck.ranks:
              self.total_cards.append(Card(i,x))


    def draw_card(self):
       card = random.choice(self.total_cards)
       self.total_cards.remove (card)
       return card
    

def handled_ace():
    ace = input(f"Would you want ace to be used as number '1' or as number '11'? ")
    if ace == '1' or ace == '11':
        return int(ace) 
    else:
        print("Enter only the number '1' or '11'.")
        return handled_ace()

    
def play_blackjack(playerhand, dealerhand, deck):
    print(f"Your current hand: {playerhand}")
    action = input("Do you want to 'Hit' or 'Stay'? ").strip().lower()


    if action == 'hit':
        new_card = deck.draw_card().card_value()
        print(f"You drew a card with value {new_card}.")
        if new_card == 11:
            new_card = handled_ace()
            
        playerhand += new_card

        if playerhand > 21:
            return "You busted! You lose."
        elif playerhand == 21:
            return "Blackjack! You win!"
        else:
            return play_blackjack(playerhand, dealerhand, deck)

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


deck = Deck()
playerhand = deck.draw_card().card_value() + deck.draw_card().card_value()
dealerhand = deck.draw_card().card_value() + deck.draw_card().card_value()
print(play_blackjack(playerhand, dealerhand, deck))