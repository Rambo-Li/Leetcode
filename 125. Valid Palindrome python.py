class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<=j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
    
""" This is my first version and it's ugly. The points I missed are 1. the while loop on line 5&7 would go out of bounds,
2. I could keep the pointers update one step at a time thus only one while loop, 3. when i==j, it is valid and don't need to check."""

# this is the better version
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True