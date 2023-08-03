class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        step = 0
        q = deque([(i,j, step) for i in range(m) for j in range(n) if grid[i][j] == 2])
        while q:
            ni, nj, step = q.popleft()
            for x,y in [(-1,0), (1,0), (0,1), (0, -1)]:
                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and grid[ni+x][nj+y] == 1:
                    q.append((ni+x, nj+y, step+1))
                    grid[ni+x][nj+y] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return step