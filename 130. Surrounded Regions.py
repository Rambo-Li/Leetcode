class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        noflip = set()
        stack = [(i,j) for i in (0, m-1) for j in range(n) if board[i][j]=='O'] + [(i,j) for j in (0, n-1) for i in range(m) if board[i][j]=='O']
        while stack:
            ni, nj = stack.pop()
            noflip.add((ni,nj))
            for x,y in [(-1, 0), (1,0), (0, -1), (0, 1)]:
                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and (ni+x, nj+y) not in noflip and board[ni+x][nj+y] == 'O':
                    stack.append((ni+x, nj+y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in noflip:
                    board[i][j] = 'X'    




        # visited = set()
        # stack = []
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O' and (i,j) not in visited:
        #             stack.append((i,j))
        #             visited.add((i,j))
        #             region = [(i,j)]
        #             flip = True
        #             while stack:
        #                 ni, nj = stack.pop()
        #                 if not ni or not nj or ni==m-1 or nj==n-1:
        #                     flip = False
        #                 for x,y in [(-1, 0), (1,0), (0, -1), (0, 1)]:
        #                     if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and (ni+x, nj+y) not in visited:
        #                         if board[ni+x][nj+y] == 'O':
        #                             stack.append((ni+x, nj+y))
        #                             region.append((ni+x, nj+y))
        #                         visited.add((ni+x, nj+y))
        #             if flip:
        #                 for k,v in region:
        #                     board[k][v] = 'X'
