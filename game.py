# Here is the description of the game simulation.

# this is a two player card game
# the game starts with a deck of cards
# the cards are dealt out to both players
# on each turn:
# both players turn over their top-most card
# the player with the higher valued card takes the cards and puts them in their scoring pile (scoring 1 point per card)
# this continues until the players have no cards left
# the player with the highest score wins
# It’s considered a simulation because the players don’t have any choice, dont worry about input
import random

class CardDeck():
    def __init__(self):
        self.suits = {'spade': 4, 'heart': 3, 'diamond': 2, 'club': 1}
        self.vals = [i for i in range(1,14)]
        self.cards = [Card(suit, val) for suit in self.suits.values() for val in self.vals]
        random.shuffle(self.cards)

class Card:
    def __init__(self, s, v): # card: (type, val)
        self.suit = s
        self.val = v
    def __gt__(self, other):
        if self.val > other.val:
            return True
        elif self.val == other.val:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False
    
    def __lt__(self, other):
        if self.val < other.val:
            return True
        elif self.val == other.val:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.card_deck = CardDeck()
        self.cards = self.card_deck.cards
    
    def get_cards(self):
        # get deck cards

        # give each player their card
        self.player1.cards = self.cards[:26]
        self.player2.cards = self.cards[26::]

    def play_game(self):
        self.get_cards()

        # each player get top of the card
        for i in range(26):
            card1 = self.player1.cards.pop()
            card2 = self.player2.cards.pop()
            
            if card1 > card2:
                self.player1.score += 1
            else:
                self.player2.score += 1
            

        # get the winner
        if self.player1.score > self.player2.score:
            print('Winner is player1')
        elif self.player1.score < self.player2.score:
            print('Winner is player2')
        else:
            print('Draw, no winner')

if __name__ == '__main__':
    test = Game()
    test.play_game()