class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = [{} for _ in range(27)] # [{}] * 27 wouldn't work
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    if (num in result[i]) or (num in result[9+j]) or (num in result[18+3*(i//3)+(j//3)]):
                        return False
                    else:
                        result[i][num] = 1
                        result[9+j][num] = 1
                        result[18+3*(i//3)+(j//3)][num] = 1
        return True
    
""" Python problematic semantic for [{}] * k costed me some debugging time. 
In this expression, very element is referenced and the same as each other. 
Update anyone would update all. """