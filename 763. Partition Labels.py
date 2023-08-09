class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        j = 0
        res = []
        found = {}
        for i, letter in enumerate(s):
            if letter not in found:
                j = max(j, s.rfind(letter))
            if i==j:
                if res:
                    res.append(j + 1 -sum(res))
                else:
                    res.append(j+1)
        return res