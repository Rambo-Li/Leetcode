class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        anchor = prices[0]
        maxProfit = 0
        for p in prices:
            if anchor < p:
                maxProfit = max(maxProfit, p-anchor)
            elif anchor > p:
                anchor = p
        return maxProfit