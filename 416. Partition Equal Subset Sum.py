class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a = set((0,))
        for k in nums:
            temp = a.copy()
            a = set()
            for i in temp:
                a.add(i+k)
                a.add(i-k)
        return 0 in a

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 ==1:
            return False
        target = total//2
        a = set((0,))
        for k in nums:
            temp = set()
            for i in a:
                if k+i == target:
                    return True
                if k+i not in a:
                    temp.add(k+i)
            a |= temp
        return False