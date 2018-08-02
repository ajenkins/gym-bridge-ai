from collections import namedtuple

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