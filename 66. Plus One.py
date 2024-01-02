class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while carry and i >=0:
            carry, digits[i] = divmod(digits[i]+carry, 10)
            i -= 1
        
        if carry == 1:
            return [1] + digits
        else:
            return digits
        
'''
Concept: for any digit, there can be a carry 1 or not
DS: one variable for carry
Algo: update while enumerating
'''