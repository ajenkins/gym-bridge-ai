from collections import namedtuple

# Cards
Card = namedtuple('Card', ['rank', 'suit'])
CLUB = 'Club'
DIAMOND = 'Diamond'
HEART = 'Heart'
SPADE = 'Spade'
CARD_SUITS = [CLUB, DIAMOND, HEART, SPADE]
JACK = 'Jack'
QUEEN = 'Queen'
KING = 'King'
ACE = 'Ace'
CARD_RANKS = list(range(2, 11)) + [JACK, QUEEN, KING, ACE]
ALL_CARDS = [Card(rank=rank, suit=suit) for rank in CARD_RANKS for suit in CARD_SUITS]

# Players
NORTH = 'North'
EAST = 'East'
SOUTH = 'South'
WEST = 'West'
PLAYERS = [NORTH, EAST, SOUTH, WEST]
NS_TEAM = (PLAYERS[0], PLAYERS[2])
EW_TEAM = (PLAYERS[1], PLAYERS[3])
TEAMS = (NS_TEAM, EW_TEAM)
TEAMMATES = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST
}

# Bidding
Contract = namedtuple('Contract', ['level', 'trump_suit'])
PASS = 'Pass'
BID_LEVELS = [1, 2, 3, 4, 5, 6, 7]
NOTRUMP = 'NoTrump'
TRUMP_SUITS = CARD_SUITS + [NOTRUMP]
BIDDING_CONTRACTS = [Contract(level=level, trump_suit=suit)
    for level in BID_LEVELS for suit in TRUMP_SUITS]
