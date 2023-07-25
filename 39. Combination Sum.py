class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i, k in enumerate(candidates):
            if target - k < 0:
                continue
            elif target - k == 0:
                res.append([k])
            else:
                temp = self.combinationSum(candidates[i:], target-k) 
                for ans in temp:
                    res.append([k] + ans)
        return res


# candidates[i:] classifies combinations as exclusive sets that definded by the smallest number. If just use candidates[:], there will be overlapping.