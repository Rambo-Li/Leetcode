class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        left = right = step = 0
        # step = 0
        # right = 0
        while right < len(nums)-1:
            temp = right
            for i in range(left, right+1):
                right = max(right, nums[i]+i)
            step += 1
            left = temp+1
        return step