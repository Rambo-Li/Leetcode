class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            dp[0][i] = i
        for j in range(1, m+1):
            dp[j][0] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]
    
"""
Concept: Two strings matching. Replace, insert, remove operation are allowed. Remove from one string equals to insert another string.
DS: A matrix representing the least steps needed for s1[:i] and s2[:j] to match
Algo: min(three operations)+1
"""