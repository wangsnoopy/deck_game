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

class Card:
    def __init__(self):
        self.types = ['spade', 'heart', 'diamond', 'club']
        self.cards = []

    def suffle_card(self):
        indexs = [i for i in range(1,14)]
        # shuffle the value first

        # give the shuffle deck card
        for i in indexs:
            for type in self.types:
                self.cards.append((type, i))
        random.shuffle(self.cards)


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
        cur_cards.suffle_card()

        # give each player their card
        for i in range(26):
            self.player1.cards.append(cur_cards.cards[i])

        for i in range(26,52):
            self.player2.cards.append(cur_cards.cards[i])

    def play_game(self):
        # each player get top of the card
        for i in range(26):
            type_one, val_one = self.player1.cards.pop()
            type_two, val_two = self.player2.cards.pop()
            # compare the val first
            if val_one > val_two:
                self.player1.score += 1
            elif val_two > val_one:
                self.player2.score += 1
            # same val
            else:
                # compare the type
                if type_one == 'spade':
                    self.player1.score += 1
                elif type_one == 'heart' and type_two != 'spade':
                    self.player1.score += 1
                elif type_one == 'diamond' and type_two == 'club':
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

    # deal the card
    game.get_cards()

    # play the game
    game.play_game()
