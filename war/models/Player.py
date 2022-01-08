# from war.models.Deck import Deck
from random import random


class Player:
    def __init__(self, num, cards):
        self._num = num
        self._deck = cards
        self._dicard_pile = []
        self._in_play = []
        self._playing = True


    @property
    def num(self):
        return self._num

    @property
    def deck(self):
        return self._deck

    @property
    def is_out_of_round(self):
        return self._is_out_of_round

    @property
    def playing(self):
        return self._playing

    @is_out_of_round.setter
    def is_out_of_round(self, value):
        self._is_out_of_round = value

    @deck.setter
    def deck(self, value):
        self._deck = value

    @playing.setter
    def playing(self, value):
        self._playing = value


    def play_card(self):
        if not self._dicard_pile and not self.deck:
            return None
        if not self.deck:
            self.deck = list(sorted(self._dicard_pile, key = lambda k: random()))
            self._dicard_pile = []

        card = self.deck.pop()
        self._in_play.append(card)
        return (card, self.num)


    def give(self):
        lossed = list(self._in_play)
        self._in_play = []
        return lossed


    def take(self, cards):
        self._dicard_pile += cards


    def show_card(self):
        return self._in_play[-1]


    def has_cards(self):
        return len(self.deck) > 0 or len(self._dicard_pile) > 0 or len(self._in_play) > 0


    def reset(self):
        self.in_war = False
        if not self.has_cards():
            self.playing = False


    def war(self):
        for _ in range(0, 3):
            card = self.play_card()
            if not card:
                break

    def __str__(self):
        sr = ''
        sr += str(self.num) + '\n'
        sr += f"deck: {str(self.deck)}\n"
        sr += f"in_play: {str(self._in_play)}\n"
        sr += f"dicard_pile: {str(self._dicard_pile)}\n"
        sr += f"_playing: {self.playing}\n"
        return sr
