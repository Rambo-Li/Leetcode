class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b != 0:
            a,b  = (a ^ b) & mask, ((a&b) << 1) & mask
        return a if a <= MAX else ~(a^mask)
    
'''
Concept: Xor captures the bits with only a one; & captures the bits with two ones; then use xor to combine together.
    Overflow, negative, and language-specific binary operations are the pain.
Algo: First the carry bits, then xor with the single one bits, and check the carry again.'''