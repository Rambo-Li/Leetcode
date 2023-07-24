class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        temp = self.subsets(nums[1:])
        return temp + [[nums[0]] + x for x in temp]