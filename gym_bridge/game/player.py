from gym_bridge.game.constants import TEAMMATES

class Player:
    declarer = False
    dummy = False
    
    def __init__(self, player, hand, is_dealer=False):
        self._player = player
        self._cards = hand
        self._teammate = TEAMMATES[self._player]
        self._dealer = is_dealer

    @property
    def dealer(self):
        return self._dealer