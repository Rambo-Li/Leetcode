class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        left = 0
        d1 = {}
        for letter in s1:
            d1[letter] = d1.get(letter, 0) + 1
        d2 = {}
        for right in range(len(s2)):
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            if right >= w:
                d2[s2[left]] -= 1
                if d2[s2[left]] == 0:
                    d2.pop(s2[left])
                left += 1
            if d1==d2:
                return True
        return False