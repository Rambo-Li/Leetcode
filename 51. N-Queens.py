class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [["."]*n for _ in range(n)]
        # excol, negdiag, posdiag = set(), set(), set()
        # res =[]
        # def backtrack(q):
        #     if q == n:
        #         res.append(["".join(a) for a in board])
        #         return
        #     for j in range(n):
        #         if (j not in excol) and (q-j not in negdiag) and (q+j not in posdiag):
        #             board[q][j] = 'Q'
        #             excol.add(j)
        #             negdiag.add(q-j)
        #             posdiag.add(q+j)

        #             backtrack(q+1)

        #             board[q][j] = '.'
        #             excol.remove(j)
        #             negdiag.remove(q-j)
        #             posdiag.remove(q+j)
        
        # backtrack(0)
        # return res

        def dfs(path, row, q):
            if q == 0:
                board = [["."]*n for _ in range(n)]
                for x,y in path:
                    board[x][y] = 'Q'
                res.append(["".join(a) for a in board])
                return
            
            for j in range(n):
                if not conflictpath(path, row,j):
                    dfs(path+((row,j),), row+1, q-1)

        def conflictpath(path, i,j):
            for x,y in path:
                if i ==x or j == y or abs(i-x)==abs(j-y):
                    return True
            return False

        res = []        
        dfs((), 0, n)
        return res