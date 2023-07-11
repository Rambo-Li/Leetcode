class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right)//2
            k = sum([ceil(a/mid) for a in piles])
            if k > h:
                left = mid + 1
                
            elif k <= h:
                res = mid
                right = mid - 1
                
        return res
    
    