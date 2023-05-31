class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "[":"]", '{':'}'}
        q = deque()
        for l in s:
            if l in ['(', '{', '[']:
                q.append(l)
            else:
                if len(q)>0:
                    t = q.pop()
                else:
                    return False
                if l != d[t]:
                    return False
        return not len(q)

""" Deque is a double ended queue. The last line is succinct. """