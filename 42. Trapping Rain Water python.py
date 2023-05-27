class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += maxLeft - height[left]               
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += maxRight - height[right]

        return result