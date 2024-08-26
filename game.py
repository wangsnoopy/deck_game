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
        self.types = ['spade', 'heart', 'diamond', 'club']
        self.vals = [i for i in range(1, 14)]

class Card:
    def __init__(self):
        self.cards = []

    def shuffle_card(self):
        vals = CardDeck().vals
        types = CardDeck().types
        for val in vals:
            for type in types:
                self.cards.append((type, val))
        random.shuffle(self.cards)

    def compare_card(self, card_one, card_two): # input card_one, card_two == (type, value)
        type_one, val_one = card_one
        type_two, val_two = card_two
        # compare the val first
        if val_one > val_two:
            return 1
        elif val_two > val_one:
            return 2
        # same val
        else:
            # compare the type
            if type_one == 'spade':
                return 1
            elif type_one == 'heart' and type_two != 'spade':
                return 1
            elif type_one == 'diamond' and type_two == 'club':
                return 1
            else:
                return 2

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
    
    def get_cards(self):
        cur_cards = Card()
        cur_cards.shuffle_card()

        # give each player their card
        for i in range(26):
            self.player1.cards.append(cur_cards.cards[i])

        for i in range(26,52):
            self.player2.cards.append(cur_cards.cards[i])

    def play_game(self):
        self.get_cards()

        # each player get top of the card
        for i in range(26):
            card_one = self.player1.cards.pop()
            card_two = self.player2.cards.pop()
            if Card().compare_card(card_one, card_two) == 1:
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
    # Create a game
    game = Game()

    # play the game
    game.play_game()