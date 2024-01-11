class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # ans = 0
        
        # def dfs(nums, value):
        #     nonlocal ans
        #     if len(nums) == 1:
        #         ans = max(ans, nums[0]+value)
        #         return
        #     for i, v in enumerate(nums):
        #         left = 1 if i==0 else nums[i-1]
        #         right = 1 if i==len(nums)-1 else nums[i+1]
        #         dfs(nums[:i]+nums[i+1:], value+v*left*right)
        # dfs(tuple(nums), ans)
        # return ans

        # # add padding to nums
        # nums = [1] + nums + [1]
        # N = len(nums)
        # # create empty cache
        # cache = [ [0]*N for _ in nums ]

        # for r in range(2,N):
        #     for l in range(r-2,-1,-1):
        #         temp = nums[l]*nums[r]
        #         # temp is here to save python from recomputing it in the loop below
        #         cache[l][r] = max( temp*nums[m] + cache[l][m] + cache[m][r] for m in range(l+1,r) )
        #     # print(cache)
        
        # return cache[0][N-1]

        dp = {}
        nums = [1] + nums + [1]
        def dfs(l, r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        return dfs(1, len(nums)-2)

"""
Concept: The key is to think about the last popped balloon to be able to break up the problem.
DS: a matrix, dp[i,j] could represent either max value from [i:j](inclusive) or [i+1:j-1](exclusive).
Algo: the last balloon gives the value i*last*j(exclusive) or (i-1)*last*(j+1)(inclusive).
    If use bottom-up dp, then the update starts from setting the right end(newest ele), then gradually expand left end.
"""