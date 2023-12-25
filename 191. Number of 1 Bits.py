class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
    
'''
Concept: count 1 bit in the binary representation
Algo: bin change n to binary string format, count method for collections
'''