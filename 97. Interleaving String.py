class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # memo = {}
        # def strip(s1, s2, s3):
        #     if not s1 and not s2 and not s3:
        #         return True

        #     if (not s3):
        #         return False
            
        #     if (s1,s2,s3) in memo:
        #         return memo[(s1,s2,s3)]

        #     if s1 and s1[0] == s3[0]:
        #         res = strip(s1[1:], s2, s3[1:])
        #         if res:
        #             memo[(s1,s2,s3)] = True
        #             return True
            
        #     if s2 and s2[0] == s3[0]:
        #         res = strip(s1, s2[1:], s3[1:])
        #         if res:
        #             memo[(s1,s2,s3)] = True
        #             return True
            
        #     memo[(s1,s2,s3)] = False
        #     return False
        
        # return strip(s2, s1, s3)

        m, n, l = len(s1), len(s2), len(s3)
        if m+n != l:
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
            # print(dp)
        return dp[-1][-1]
    
"""
Concept: a char in a string can match any char of other two strings, after the match, do it again without both matched char.
DS: matrix recording if s3[:i+j] can be matched with s1[:i] and s2[:j], with two strings as dimensions. This boolean value is a genius design.
Algo: whether s1[i] and s2[j] can match s3[i+j] depends on if the last char match as well as if the strings without last char match."""