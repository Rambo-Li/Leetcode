class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, pattern = {}, {}
        
        for c in t:
            pattern[c] = pattern.get(c, 0) +1
        
        left, right, minLen = 0, 0, 100000
        resLeft, resRight = -1, -2
        
        have, need = 0, len(pattern)
        
        for i in range(len(s)):
            if s[i] in pattern:
                window[s[i]] = window.get(s[i], 0) + 1
                if window[s[i]] == pattern[s[i]]:
                    have += 1
            while have == need:
                right = i
                if minLen > right - left:
                    minLen = right - left
                    resLeft, resRight = left, right
                if s[left] in pattern:
                    window[s[left]] -= 1
                    if window[s[left]] < pattern[s[left]]:
                        have -= 1
                    left += 1
                else:
                    left += 1
                    
        return "" if resLeft == -1 else s[resLeft:resRight+1]