class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)<=2:
        #     return max(nums)
        n2 = nums.copy()
        for i in range(2, len(nums)-1):
            nums[i] = max(nums[0:i-1])+nums[i]
        for i in range(3, len(nums)):
            n2[i] = max(n2[1:i-1]) + n2[i]

        return max(nums[-3:]+ n2[-2:])