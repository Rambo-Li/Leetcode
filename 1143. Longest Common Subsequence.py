class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

"""
Concept: if two letters are the same, defer to s[i-1]&s2[j-1]; if not, check s[i]&s2[j-1] or s[i-1]&s2[j].
DS: one matrix
Algo: how to formulate the current steps given all former steps, base on two senarios: current character equal or not
"""