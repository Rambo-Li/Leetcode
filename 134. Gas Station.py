class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        # net = [gas[i] - cost[i] for i in range(len(gas))]
        start = currgas = 0
        for stop in range(len(gas)):
            currgas += gas[stop] - cost[stop]
            if currgas < 0:
                currgas = 0
                start = stop + 1
        return start