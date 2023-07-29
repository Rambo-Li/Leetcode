class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = maxp = minp = nums[0]
        for i in range(1, len(nums)):
            temp1, temp2 = minp, maxp
            minp = min(nums[i]*temp1, nums[i]*temp2, nums[i])
            maxp = max(nums[i]*temp1, nums[i]*temp2, nums[i])
            res = max(res, maxp)
        return res