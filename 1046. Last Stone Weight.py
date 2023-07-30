class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-a for a in stones]
        heapify(s)
        while len(s)>1:
            a = -heappop(s)
            b = -heappop(s)
            if a > b:
                heappush(s, b-a)
        return -s[0] if s else 0