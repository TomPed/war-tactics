from operator import attrgetter

class Game:
	def __init__(self, players):
		self.players = players
		self.war = 1
		self.pile = []

	def is_pile_draw(self):
		pass

	def simulate(self):
		for player in self.players:
			player.is_out_of_round = False
		while not self._is_game_over():
			self.war -= 1

			for player in self.players:
				if player.has_cards() and not player.is_out_of_round:
					self.pile.append(player.play())

			if self.war > 0:
				continue
			if self.is_pile_draw() and self.war == 0:
				self._set_in_round()
				self.war = 4
				continue




			winning_player_num = self._get_round_winner()

			for player in self.players:
				self._get_player(winning_player_num).take(player.give())

			for player in self.players:
				player.is_out_of_round = False

			for player in self.players:
				print(player)

	def _get_player(self, num):
		for player in self.players:
			if player.num == num:
				return player


	def _set_in_round(self):
		max_val = -1
		for player in self.players:
			last_card = player.show_card()
			if last_card > max_val:
				max_val = last_card

		for player in self.players:
			if player.show_card() != max_val:
				player.is_out_of_round = True

	def _get_round_winner(self):
		end = {}
		max_val = -1
		for player in self.players:
			last_card = player.show_card()
			if last_card > max_val:
				max_val = last_card
			end[last_card] = player.num

		return end[max_val]



	def _is_game_over(self):
		return Game.SINGLE_TRUE(map(lambda p: p.has_cards(), self.players))

	def SINGLE_TRUE(iterable):
		i = iter(iterable)
		return any(i) and not any(i)
