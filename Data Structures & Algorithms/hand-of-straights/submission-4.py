class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        hand.sort()

        for card in hand:
            if freq[card]:
                for i in range(card, card + groupSize):
                    if not freq.get(i):
                        return False
                    freq[i] -= 1
        return True