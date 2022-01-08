class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit
