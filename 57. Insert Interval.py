class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, inter in enumerate(intervals):
            if newInterval[1] < inter[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > inter[1]:
                res.append(inter)
            else:
                newInterval = [min(newInterval[0], inter[0]), max(inter[1], newInterval[1])]
        res.append(newInterval)
        return res
    
# Great disecting of the scenerios.