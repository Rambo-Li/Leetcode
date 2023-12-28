class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res<<1 | n&1
            n = n >> 1
        return res

'''
Concept: each time get one bit from a number and give it to another number
Algo: masking to the the bit, and shifting to set the bit on new number
    integer and work on bits with bit operator and reverse a list can use [::-1]
'''