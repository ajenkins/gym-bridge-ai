from collections import namedtuple

# Cards
Card = namedtuple('Card', ['rank', 'suit'])
CARD_SUITS = ['Club', 'Diamond', 'Heart', 'Spade']
CARD_RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
ALL_CARDS = [Card(rank=rank, suit=suit) for rank in CARD_RANKS for suit in CARD_SUITS]

# Bidding
Contract = namedtuple('Contract', ['level', 'trump_suit'])
BID_LEVELS = [1, 2, 3, 4, 5, 6, 7]
TRUMP_SUITS = CARD_SUITS + ['NoTrump']
BIDDING_CONTRACTS = [Contract(level=level, trump_suit=suit)
    for level in BID_LEVELS for suit in TRUMP_SUITS]
