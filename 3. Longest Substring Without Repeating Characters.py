class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        count, left = 0, 0
        for i, letter in enumerate(s):
            if letter in d:
                count = max(count, i - left)
                left = d.get(letter) + 1 if left<=d.get(letter) else left
            d[letter] = i
        return max(count, len(s) - left)