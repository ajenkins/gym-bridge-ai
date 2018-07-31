from gym_bridge.game.contracts.bidding_contract import BiddingContract
from gym_bridge.game.constants import BIDDING_CONTRACTS, PASS

class AmericanStandard(BiddingContract):

    def call(self, hand, previous_bids):
        # TODO: Implement real bidding
        return PASS
