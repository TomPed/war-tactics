# from war.models.Deck import Deck
from random import shuffle, random


class Player:
	def __init__(self, num):
		self._num = num
		self._deck = []
		self._dicard_pile = []
		self._in_play = []
		self._init()
		self.is_out_of_round = None

	@property
	def num(self):
		return self._num

	@property
	def deck(self):
		return self._deck

	@property
	def is_out_of_round(self):
		return self._is_out_of_round

	@is_out_of_round.setter
	def is_out_of_round(self, value):
		self._is_out_of_round = value

	@deck.setter
	def deck(self, value):
		self.deck = value

	def _init(self):
		for _ in range (0, 4):
			for j in range(0, 15):
				self.deck.append(j)

		shuffle(self.deck)

	def shuffle(self):
		self._deck = sorted(self.dicard_pile, key = lambda k: random.random())
		self.dicard_pile = []


	def play(self):
		if not self._dicard_pile and not self.deck:
			exit(1)
		if not self.deck:
			self.deck = sorted(self._dicard_pile, key = lambda k: random())
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



	def war(self):
		for _ in range(0, 3):
			card = self.play()
			if not card:
				break



		c = self._deck.draw()
		self.in_play(c)
		return c

	def __str__(self):
		sr = ''
		sr += str(self.num) + '\n'
		sr += f"deck: {str(self.deck)}\n"
		sr += f"in_play: {str(self._in_play)}\n"
		sr += f"dicard_pile: {str(self._dicard_pile)}\n"
		sr += f"is_out_of_round: {self.is_out_of_round}\n"
		return sr
