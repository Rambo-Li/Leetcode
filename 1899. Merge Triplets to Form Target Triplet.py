class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def fil(trip1):
            nonlocal target
            if trip1[0]>target[0] or trip1[1] > target[1] or trip1[2] > target[2]:
                return [-1000, -1000, -1000]
            else:
                return trip1

        def merge(trip1, trip2):
            x, y, z = fil(trip1)
            x1, y1, z1 = fil(trip2)
            return [max(x, x1), max(y, y1), max(z, z1)]
        
        return reduce(merge, triplets) == target
    
        x, y, z = -inf, -inf, -inf
        for trip in triplets:
            x1, y1, z1 = trip
            if x1<=target[0] and y1 <= target[1] and z1 <= target[2]:
                x, y, z = max(x, trip[0]), max(y, trip[1]), max(z, trip[2])
        return [x, y, z] == target

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3