class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(2, m+1, 2):
            if p[j-1] == "*":
                dp[j][0] = dp[j-2][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    if p[i-2] == s[j-1] or p[i-2]==".":
                        dp[i][j] = dp[i][j-1] or dp[i-2][j]
                    else:
                        dp[i][j] = dp[i-2][j]
        # print(dp)
        return dp[-1][-1]
"""
Concept: Two strings matching. The transition is to think if a condition is true, what happens to the two strings.

"""