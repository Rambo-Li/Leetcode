class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for h in heights:
            a = 0
            temp = []
            if stack and h < stack[-1]:
                while stack and h < stack[-1]:
                    temp.append(stack.pop())
                    a += 1
                temp = sorted(temp)
                l = len(temp)
                v = None
                for i in range(l):
                    if v != temp[i]:
                        v = temp[i]
                        maxArea = max(maxArea, (l-i) * v)
                for i in range(a):
                    stack.append(h)

            stack.append(h)
            
        l = len(stack)
        v = None
        for i in range(len(stack)):
            if v != stack[i]:
                v = stack[i]
                maxArea = max(maxArea, (l-i)*v)
            
        return maxArea

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
    
# The better solution utilized the index, while the other one uses extra variable to keep track of the width.
# The key semantic is to keep track of the left side of the rectangle when push to stack