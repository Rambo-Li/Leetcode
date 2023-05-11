class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable=dict()
        for i, value in enumerate(nums):
            if (target - value) in hashtable:
                return [i, hashtable[target-value]]
            else:
                hashtable[value] = i 


""" Flipping array index and value """