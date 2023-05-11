class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        # This is the priority queue solution
        h = []
        for n, count in d.items():
            if len(h) < k:
                heapq.heappush(h, (count, n))
            else:
                heapq.heappushpop(h, (count, n))
        return [k for _, k in h]
                
        # This is the plain sort solution
        res = sorted(d.items(), key = lambda x : x[1], reverse = True)
        return [x[0] for x in res[:k]]
    
    """ There is a seletion sort version solution for this problem. """