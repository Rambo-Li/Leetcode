class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(1, n+1):
            res[i] = res[i//2] + (i&1)
        return res
    
'''
Concept: deduction - even number contains the same amount of ones as i//2, odd number contains the amount of ones as i//2+1
    how to flip between odd and even
Algo: we can use a flag to indicate odd or even, or use the last bit (&1)
'''