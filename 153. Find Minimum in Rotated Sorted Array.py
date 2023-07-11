class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = None
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < nums[right] and nums[mid] < nums[left]:
                res = nums[mid]
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] >= nums[left]:
                return min(res, nums[left]) if res!=None else nums[left]
            # else:
            #     return min(res, nums[mid]) if res!=None else nums[mid]
        return res