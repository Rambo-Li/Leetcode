class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        temp = sorted(zip(position, speed))
        tar = (target - temp[-1][0]) / temp[-1][1]
        while temp:
            pos, sp = temp.pop()
            if (target - pos) / sp > tar:
                res += 1
                tar = (target - pos) / sp
        return res