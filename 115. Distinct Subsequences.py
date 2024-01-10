class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp = [[0] * (len(t)+1) for _ in range(len(s) + 1)]

        # for i in range(len(dp)):
        #     dp[i][0] = 1
        
        # for i in range(1, len(dp)):
        #     for j in range(1, len(dp[0])):
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # print(dp)
        # return dp[len(s)][len(t)]
    
        m, n = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if t[i-1] != s[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        return dp[-1][-1]

"""
Concept: Two strings matching. The dp matrix means how many possibilities s[:i] and t[:j] can match
DS: The dp matrix, representing how many ways s[:i] and t[:j] can match
Algo: dp[i][j] = dp[i-1][j-1] + dp[i][j-1], diagonal+(s-1)
"""