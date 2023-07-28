class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        res = [1]*(len(s)+1)
        for i in range(1, len(s)):
            if int(s[i-1:i+1]) <= 26 and s[i]!= '0' and s[i-1]!='0':
                res[i+1] = res[i] + res[i-1]            
            elif (int(s[i-1:i+1]) > 26 or s[i-1]== '0') and s[i]== '0' :
                return 0
            elif s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                res[i+1] = res[i]
            else:
                res[i+1] = res[i-1]
        return res[-1]
    

# This problem has way more scenarios than I thought.