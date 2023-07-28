class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [math.inf] * (amount+1)
        res[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    res[i] = min(res[i], res[i-c]+1)
        
        return -1 if res[-1]==math.inf else res[-1]

# What I learned from this problem is DP update in a for loop.