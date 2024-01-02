class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res = 1
        # flag = 1 if n >=0 else -1
        # n *= flag
        # exps = []
        # while n:
        #     exp = 1
        #     base = 2
        #     while n >= base:
        #         base *= 2
        #         exp += 1
        #     n -= base//2
        #     exps.append(exp-1)
        # for exp in exps:
        #     temp = x
        #     for i in range(exp):
        #         temp *= temp
        #     res *= temp
        
        # return res if flag==1 else 1/res

        if n < 0: 
            x = 1 / x 
            n = -n 
        result = 1 
        current_product = x 
        while n > 0: 
            if n % 2 == 1: 
                result = result * current_product 
            current_product = current_product * current_product 
            n = n // 2 
        return result 

'''
Concept: decompose a integer to the power of 2's
DS: one variable store the odd number of x, another stores the even number of x
Algo: even number will become 1 at the end, and two results are combined together
    need to update n, odd, even
'''