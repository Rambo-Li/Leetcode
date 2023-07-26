class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(path, leftword):
            if not leftword:
                res.append(path)
                return
            for j in range(1, len(leftword)):
                if ispanlindrome(leftword[:j+1]):
                    dfs(path+[leftword[:j+1]], leftword[j+1:])
            dfs(path+[leftword[0]], leftword[1:])
        
        def ispanlindrome(s):
            left, right = 0, len(s)-1
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        res = []
        dfs([], s)
        return res