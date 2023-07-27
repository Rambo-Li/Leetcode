class Solution:
    def climbStairs(self, n: int) -> int:

        res = [1] * (n+1)
        for i in range(2, n+1):
            res[i] = res[i-2] + res[i-1]
        return res[n]