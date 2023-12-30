class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        res = 0
        while x:
            if res < MIN_INT/10 or res > MAX_INT/10:
                return 0
            if x > 0:
                x, r = divmod(x, 10)
            elif x < 0:
                x, r = divmod(x, -10)
                x *= -1
            res = res*10 + r            
        
        return res 

'''
Concept: get each digit of a number, and build a number through digit
Algo: %positive number, %negative number
'''