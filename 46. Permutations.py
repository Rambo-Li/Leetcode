class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        temp = self.permute(nums[1:])
        return [ans[:i] + [nums[0]] + ans[i:] for ans in temp for i in range(len(ans)+1) ]