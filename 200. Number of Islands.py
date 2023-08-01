class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        stack = []
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island += 1
                    stack.append((i,j))
                    while stack:
                        ni, nj = stack.pop()
                        visited.add((ni,nj))
                        if grid[ni][nj] == '1':
                            for x,y in [(-1,0), (1,0), (0,1), (0,-1)]:
                                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and (ni+x, nj+y) not in visited:
                                    stack.append((ni+x, nj+y))
        return island