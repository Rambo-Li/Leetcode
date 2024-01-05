class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo = {}    
        # def dp(nums, target):
        #     if len(nums) == 1:
        #         res = 0
        #         if target == nums[0]:
        #             res +=1 
        #         if target == -nums[0]:
        #             res += 1
        #         return res

        #     if (tuple(nums), target) in memo:
        #         return memo[(tuple(nums),target)]
        #     a = dp(nums[:len(nums)-1], target -nums[-1])
        #     b = dp(nums[:len(nums)-1], target + nums[-1])            
        #     memo[(tuple(nums), target)] = a+b
        #     return a+b        
        # return dp(nums, target)
        
        #2 use a dict, set possible outcome as the key and count as the value
        # res = {0:1}
        # for num in nums:
        #     temp = {}
        #     for curSum in res:
        #         temp[curSum + num] = temp.get(curSum + num,0) + res[curSum]
        #         temp[curSum - num] = temp.get(curSum - num,0) + res[curSum]
        #     res = temp
        # return res.get(target,0)

        #3 treat this problem as chosing k elements to sum to total+target
        if target<0:
            target *= -1
        summ = sum(nums)
        if summ < target or (summ+target)%2==1:
            return 0
        new_target = (summ+target)//2
        dp = [1] + [0] * (new_target)
        for num in nums:
            for j in range(new_target, num-1, -1):
                dp[j] += dp[j-num]
        return dp[-1]
    
"""
Concept: one dimension is how many ways can be reached for each total(target is the end), adding a new number, meaning that
    total i has added ways from (i-new), plus the ways originally reached i.
DS: an array of length target
Algo: different from coin problems, each element can only be picked once or zero, so the update is from the end of the array.
    The array represents pathes of all the elements before current, by adding current, (i-current) can reach i now, plus whatever ways i already have.
"""