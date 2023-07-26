class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if not digits:
            return []
        
        temp = self.letterCombinations(digits[1:])
        if not temp:
            temp = [""]
        return [a+b for a in d[int(digits[0])] for b in temp]
