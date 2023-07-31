class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums[:k]
        heapify(res)
        for i in nums[k:]:
            if i > res[0]:
                heappushpop(res, i)
        return res[0]