from operator import attrgetter

class Game:
    def __init__(self, players):
        self.players = players
        self.war = 1
        self.pile = []
        self._rounds = 0

    def is_pile_draw(self):
        pass

    def simulate(self):
        while True:
            self._rounds += 1
            for p in self.players:
                p.reset()
            in_play_players = list(filter(lambda p: p.playing, self.players))
            for p in in_play_players:
                print(p)
            if len(in_play_players) == 1:
                print(f"ending{self._rounds}")
                exit(0)

            for p in in_play_players:
                p.play_card()


            while self._is_war():
                for p in in_play_players:
                    p.war()


            for p in in_play_players:
                print(p)

            winner = self._get_winning_player()


            for p in in_play_players:
                winner.take(p.give())


            for p in in_play_players:
                print(p)


    def _is_war(self):
        in_play_players = filter(lambda p: p.playing, self.players)
        max_card = - 1
        is_war = False
        for p in in_play_players:
            card = p.show_card()
            if card == max_card:
                is_war = True
            if card > max_card:
                max_card = card

        if is_war:
            for p in in_play_players:
                if p.show_card == max_card:
                    p.in_war = True

        return is_war


    def _get_winning_player(self):
        in_play_players = list(filter(lambda p: p.playing, self.players))
        max_card = - 1
        for p in in_play_players:
            card = p.show_card()
            if card > max_card:
                max_card = card

        for p in in_play_players:
            if p.show_card() == max_card:
                return p
