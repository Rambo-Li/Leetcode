class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index in range(len(nums)):
            if nums[index] > 0:
              break
            if index > 0 and nums[index] == nums[index-1]:
              continue
            i,j = index+1, len(nums)-1
            while i < j:
                if nums[i] + nums[j] + nums[index] > 0:
                    j -=1
                elif nums[i] + nums[j] + nums[index] < 0 :
                    i += 1
                else:
                    if [nums[index], nums[i], nums[j]] not in res:
                        res.append([nums[index], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < j:
                      i += 1
                
        return res
    
""" The best solution use the divide and conquer concept. Dividing the numbers around zero, run O(n^2) on each."""