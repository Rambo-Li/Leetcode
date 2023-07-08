class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        q = []
        for i, t in enumerate(temperatures):
            if q and  q[-1][0] < t:
                while q and q[-1][0] < t:
                    _, j = q.pop()
                    res[j] = i - j
            q.append((t, i))
        return res