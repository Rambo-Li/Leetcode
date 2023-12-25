class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y, nums)

'''
Concept: duplicate numbers except for one
Algo: XOR same number twice gives zero
'''