class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back = 1, 1
        l = len(nums)
        result = [1]* l
        for i in range(l):
            result[i] *= front
            result[l -1 - i] *= back
            front *= nums[i]
            back *= nums[l - 1 -i]
        return result
    
    """ Original solution is to build two arrays, one from front and one from back, then zip them together. This one pass solution requires less space and is more fun."""