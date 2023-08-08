class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand.sort()
        # while hand:
        #     first = hand[0]
        #     for i in range(groupSize):
        #         try:
        #             hand.remove(first + i)
        #         except:
        #             return False
        # return True

        heapify(hand)
        side = []
        while hand:
            first = heappop(hand)
            i = 1
            while i < groupSize:
                if not hand:
                    return False
                temp = heappop(hand)
                if temp == first + i:
                    i += 1
                elif temp >= first + groupSize:
                    return False
                else:
                    side.append(temp)
            while side:
                heappush(hand, side.pop())
        return True