class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        temp = self.subsetsWithDup(nums[1:])
        return temp + [sorted([nums[0]] + a) for a in temp if sorted([nums[0]] + a) not in temp]