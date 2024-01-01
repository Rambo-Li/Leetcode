class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i, l in enumerate(matrix):
            for j,n in enumerate(l):
                if n == 0:
                    rows.add(i)
                    cols.add(j)
        # for row in rows:
        #     matrix[row] = [0]*len(matrix[0])
        # for l in matrix:
        #     for col in cols:
        #         l[col] = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in rows or c in cols:
                    matrix[r][c] = 0

'''
Concept: how to use less memory to represent a set of (i,j)
DS: use two sets to store i's and j's, O(N+M). The optimal solution is to reflect any 0 to the border line while keeping two flags for the border line themselves.
'''