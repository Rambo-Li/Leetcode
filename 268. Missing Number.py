class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

'''
Concept: N consecutive numbers sum up to n*(n+1)/2
Algo: sum of all minus there are equals the missing one
'''