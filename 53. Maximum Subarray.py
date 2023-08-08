class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        res = nums[0]
        for right in range(len(nums)):
            currsum += nums[right]
            res = max(res, currsum)
            if currsum < 0:
                currsum = 0
            
        return res