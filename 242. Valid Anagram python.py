class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            d[t[i]] = d.get(t[i],0) - 1
        for c in d.values():
            if c != 0:
                return False
        return True

""" The hack way is to build a 26 slot array. Using letters as index (ord function). But it can't work with a bigger alphabet. """