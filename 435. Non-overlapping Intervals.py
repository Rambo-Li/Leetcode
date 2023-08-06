class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l, r = intervals[0]
        res = 0
        # print(intervals)
        for inter in intervals[1:]:
            if inter[0] < r and inter[1] >= r:
                res += 1
            elif inter[0] < r and inter[1] < r:
                res += 1
                r = inter[1]
            elif inter[0] >= r:
                l, r = inter
            # else:
            #     l, r = inter
        return res