from gym_bridge.game.constants import BIDDING_CONTRACTS

class BiddingContract:

    @classmethod
    def call(cls, hand, previous_bids):
        raise NotImplementedError