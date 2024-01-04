class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
            
        return dp[-1]
    
"""
Concept: total coin path equals path without this coin value plus path at (amount - coin) with this coin value
DS: a array of length (amount)
Algo: for each coin value, update the array once, which gives the path of coin value so far,
    for the next coin value, the path only needs to add the path of (amount - coin)
"""