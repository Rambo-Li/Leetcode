class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        stack = []
        maxcount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i,j))
                    count = 0
                    while stack:
                        ni, nj = stack.pop()                        
                        if grid[ni][nj] == 1:
                            count += 1
                            for x,y in [(-1,0), (1,0), (0,1), (0,-1)]:
                                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0:
                                    stack.append((ni+x, nj+y))
                            grid[ni][nj] = 0
                    maxcount = max(maxcount, count)
        return maxcount