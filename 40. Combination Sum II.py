class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        for i, k in enumerate(candidates):
            if target - k < 0 or (i!=0 and k==candidates[i-1]):
                continue
            elif target - k == 0:
                if [k] not in res:
                    res += [[k]]
            else:
                temp = self.combinationSum2(candidates[i+1:], target - k)
                res += [[k]+ a for a in temp]
        return res