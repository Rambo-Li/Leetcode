class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        left = 0
        res = []
        for right in range(len(nums)):
            while q and q[-1] < nums[right]:
                q.pop()
            q.append(nums[right])

            if right - left + 1 > k:
                if nums[left] >= q[0]:
                    q.popleft()
                left += 1
            if right - left + 1 == k:
                res.append(q[0])
        return res