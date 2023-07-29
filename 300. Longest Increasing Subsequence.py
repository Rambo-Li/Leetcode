class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr = [nums[0]]
        for i in nums:
            if i > curr[-1]:
                curr.append(i)
            else:
                idx = bisect_left(curr, i)
                curr[idx] = i
        return len(curr)




        # res = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     j = i-1
        #     while j>=0:
        #         if nums[j] < nums[i]:
        #             res[i] = max(res[i], res[j]+1) 
        #         j -= 1
        # return max(res)

# A simple array-like data structure with clever update rule.