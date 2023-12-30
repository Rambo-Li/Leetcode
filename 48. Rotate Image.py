class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # method 1: rotate four corners
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                matrix[l+i][r], matrix[r][r-i], matrix[r-i][l], matrix[l][l+i] = matrix[l][l+i], matrix[l+i][r], matrix[r][r-i], matrix[r-i][l]
            r -= 1
            l += 1
        
        # method 2: zip is a great way to do transpose
        matrix[:]=[i[::-1] for i in zip(*matrix)]

        # method 3: do a line change and a elment swap
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]

'''
Concept: the indexes are related and represent by enumeration variables
Algo: the key is to get the variable-expressed indexes correct
  The zip function is suitable for transpose purposes, even it actually created a new matrix'''