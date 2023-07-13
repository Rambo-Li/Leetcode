class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        elif timestamp > self.map[key][-1][0]:
            self.map[key] += [(timestamp, value)]
        # else:
        #     self.map[key] += [(timestamp, value)]
        #     self.map[key].sort()
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        times = self.map[key]
        left, right = 0, len(times)-1
        res = None
        while left <= right:
            mid = (left+right)//2
            if times[mid][0] < timestamp:
                res = mid
                left = mid + 1
            elif times[mid][0] > timestamp:
                right = mid -1
            else:
                return times[mid][1]
        if res != None:
            return times[res][1]
        return ""