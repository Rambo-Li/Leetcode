class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canreach, l = 0, len(nums)-1
        for i in range(len(nums)):
            canreach = max(canreach, i+nums[i])
            if canreach >= l:
                return True
            elif canreach== i :
                return False