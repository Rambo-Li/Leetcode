class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        # l, r = intervals[0]
        h = []
        # heapify(h)
        res = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <=q:
                l, r = intervals[i]
                heappush(h, (r - l + 1, r))
                i += 1
            while h and h[0][1] < q:
                heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[a] for a in queries]



class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    
        intervals.sort(key = lambda x:x[1]-x[0])
        q = sorted([qu,i] for i,qu in enumerate(queries))
        res=[-1]*len(queries)
        
        for left,right in intervals:
            ind = bisect.bisect(q,[left])
            while ind<len(q) and q[ind][0]<=right:
                res[q.pop(ind)[1]]=right-left+1
        return res

# Two solutions, one is a genius way of using heap, the other is sorting by distance then pop all q fits in it, but it still needs binary search the whole queries very time.