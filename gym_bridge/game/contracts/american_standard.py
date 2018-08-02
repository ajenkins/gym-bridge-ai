from gym_bridge.game.contracts.bidding_contract import BiddingContract
from gym_bridge.game.constants import (
    BIDDING_CONTRACTS, PASS, JACK, QUEEN, KING, ACE, CLUB, DIAMOND, HEART, SPADE
    )


class AmericanStandard(BiddingContract):

    @classmethod
    def call(cls, player, partner, hand, previous_bids):
        """Returns PASS or a bid"""
        points = cls._calculate_points(hand)
        if cls._bid_count(player, partner, previous_bids) == 0:
            if points < 12:
                return PASS
            elif 12 <= points <= 21:
                pass
        return PASS

    @staticmethod
    def _bid_count(player, partner, previous_bids):
        """How many bids have been placed so far between you and your partner"""
        return 0

    @staticmethod
    def _calculate_points(hand):
        total = 0
        for card in hand:
            if card.rank == JACK:
                total += 1
            elif card.rank == QUEEN:
                total += 2
            elif card.rank == KING:
                total += 3
            elif card.rank == ACE:
                total += 4
        return total

    @staticmethod
    def _num_cards_of_suit(suit, hand):
        """Return the number of cards in the hand of the given suit"""
        return sum(1 for card in hand if card.suit == suit)

    @classmethod
    def _n_card_major(cls, n, hand):
        """Returns True or False if hand contains an at least n cards in a major suit"""
        return cls._num_cards_of_suit(HEART, hand) >= n or cls._num_cards_of_suit(SPADE, hand)

    @staticmethod
    def _n_card_minor(n, hand):
        """Returns True or False if hand contains an at least n cards in a minor suit"""
        return cls._num_cards_of_suit(CLUB, hand) >= n or cls._num_cards_of_suit(DIAMOND, hand)
