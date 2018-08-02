from collections import namedtuple
from gym_bridge.game.constants.cards import CARD_SUITS

Contract = namedtuple('Contract', ['level', 'trump_suit'])
PASS = 'Pass'
BID_LEVELS = [1, 2, 3, 4, 5, 6, 7]
NOTRUMP = 'NoTrump'
TRUMP_SUITS = CARD_SUITS + [NOTRUMP]
BIDDING_CONTRACTS = [Contract(level=level, trump_suit=suit)
    for level in BID_LEVELS for suit in TRUMP_SUITS]