class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = [("(", n-1, n)]
        res = []
        while temp:
            t = temp.pop()
            if t[1] == t[2] and t[2]!=0:
                temp.append((t[0]+"(", t[1]-1, t[2]))
            elif t[1] < t[2] and t[1]>0:
                temp.append((t[0]+"(", t[1]-1, t[2]))
                temp.append((t[0]+")", t[1], t[2]-1))
            elif t[1] < t[2] and t[1] ==0:
                temp.append((t[0]+")", t[1], t[2]-1))
            elif t[2] == 0:
                res.append(t[0])
        return res