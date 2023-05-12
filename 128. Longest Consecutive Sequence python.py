class Solution:
    def longestConsecutive(self, nums) -> int:
        d = dict()
        result = 0
        for num in nums:
            if num not in d: # duplicate can't go in and cause any update
                if (num-1 in d) and (num+1 in d):
                    r, l = d[num+1], d[num-1]
                    d[d[num-1]], d[d[num+1]]  = d[num+1], d[num-1]
                    d[num] = num
                    result = max(result, r - l + 1)
                elif num-1 in d:
                    r, l = num, d[num - 1]
                    d[d[num-1]], d[num] = num, d[num - 1]
                    result = max(result, r - l + 1)
                elif num +1 in d:
                    l, r = num, d[num+1]
                    d[d[num+1]], d[num] = num, d[num+1]
                    result = max(result, r - l + 1)
                else:
                    d[num] = num
                    result = max(result, 1)
        return result

""" The idea is to keep ranges in the memory, the key and the value represent two end points of the range. If the key is the 
left end, then the value is the right end, and vice versa. When a number merges with a range, update the left and right end.
The update needs extra care, because merging with a true range and merging with a single number is different. This is where I 
spent most of debugging time. After merging, only the end points have the correct number, that's why duplicates are harmful."""

# This is the other hot solution that everyone uses
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        count=0
        for n in nums:
            if (n-1) not in numset:
                length=0
                while (n+length) in numset:
                    length+=1
                count=max(count,length)
        return count