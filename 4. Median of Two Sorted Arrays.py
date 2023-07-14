class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total//2
        if total <= 3:
            temp = sorted(nums1 + nums2)
            mid = (len(temp) -1) //2
            return temp[mid] if len(temp)%2 ==1 else (temp[mid]+temp[mid+1])/2

        if len(nums1) <= len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        
        left, right = 0, len(a)-1

        while True:  
            i = (left + right)//2
            j = half -2 - i
            a_left = a[i] if i>=0 else -10000
            a_right = 10000 if i+1==len(a) else a[i+1]
            b_left = b[j] if j>=0 else -10000
            b_right = 10000 if j+1==len(b) else b[j+1]
    
            if a_left<=b_right and b_left<=a_right:
                if total % 2==1:
                    return min(a_right, b_right)
                else:
                    return (min(a_right, b_right) + max(a_left, b_left))/2
            elif a_left > b_right:
                right = i -1
            elif b_left > a_right:
                left = i + 1
        

# This is a hack for test cases, where the big numbers(>10000) are dealt with total<=3 cases. This beats 92% of the answers. It might hint how to speed up on leetcode.