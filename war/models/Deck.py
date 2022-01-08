from random import shuffle

from war.models.Card import Card

class Deck:
	def __init__(self):
		self.hand = self._init()
		self.discard_pile = []

	def _init(self):
		res = []
		for i in range(2, 15):
			for j in ['C', 'D', 'H', 'S']:
				res.append(Card(i, j))
		return shuffle(res)

	def draw(self):
		if not self._to_play:
			self.to_play = shuffle(self._played)
			self._played = []
		return self._to_play.pop()

	def add_to(self, cards):
		for c in cards:
			self.played.append(c)

	def is_empty(self):
		return not self._to_player and not self._played
