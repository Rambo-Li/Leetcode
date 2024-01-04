class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*3 for _ in range(len(prices)+1)]
        dp[0][0] = -inf
        for i in range(1, len(prices)+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0]+prices[i-1]
        return max(dp[-1])
    
"""
Concept: Using state as the other dimension of the dp matrix, capturing max values for all states at any time
    Say if a future time max requires present time to be a "cooldown", then it can the max value for 'cooldown'
DS: dp matrix, state * data
Algo: find the correct state transition. For this problem, the key is to store the buyin price as a neg number to max value,
    later on, just add the current price to get the profit. Otherwise this buyin price need to be carried along some way.
"""