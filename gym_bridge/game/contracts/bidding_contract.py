from gym_bridge.game.constants import BIDDING_CONTRACTS

class BiddingContract:

    def call(self, hand, previous_bids):
        raise NotImplementedError