class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        leftstack, rightstack = [intervals[0][0]], [intervals[0][1]]
        for left, right in intervals:
            if left > rightstack[-1] or right < leftstack[-1]:
                leftstack.append(left)
                rightstack.append(right)
            else:
                while leftstack and rightstack and not (left > rightstack[-1] or right < leftstack[-1]):
                    l = leftstack.pop()
                    r = rightstack.pop()
                    left, right = min(l, left), max(r, right)
                leftstack.append(left)
                rightstack.append(right)
        res = []
        for i in range(len(leftstack)):
            res.append([leftstack[i], rightstack[i]])
        return res
            