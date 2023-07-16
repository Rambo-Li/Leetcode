class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        left = 0
        mostLetter = 0
        res = 0
        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            mostLetter = max(mostLetter, d[s[right]])

            if right - left + 1 - mostLetter <= k:
                continue
            else:
                # res = max(res, right-left)
                d[s[left]] -= 1
                # mostLetter = max(d.values())
                left += 1
        return right - left + 1 #max(res, right-left+1)
    
# This one is tricky. The best solution thinks about the position, instead of the letter itself, and use the maximum window size to test next window.