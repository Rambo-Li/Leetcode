class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        isPac = [[True if i==0 or j==0 else False for j in range(n)] for i in range(m)]
        isAtl = [[True if i==m-1 or j==n-1 else False for j in range(n)] for i in range(m)]

        pacStack = [(0,j) for j in range(n)] + [(i,0) for i in range(m)]
        pacStack.remove((0,0))
        atlStack = [(i,n-1) for i in range(m)] + [(m-1,j) for j in range(n)]
        atlStack.remove((m-1, n-1))

        while pacStack:
            ni, nj = pacStack.pop()
            for x,y in [(-1,0), (1,0), (0, -1), (0,1)]:
                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and not isPac[ni+x][nj+y]:
                    if heights[ni][nj] <= heights[ni+x][nj+y]:
                        isPac[ni+x][nj+y] = True
                        pacStack.append((ni+x, nj+y))
        
        res = []
        while atlStack:
            ni, nj = atlStack.pop()
            if isPac[ni][nj]: # and (ni,nj) not in res:
                res.append((ni,nj))
            for x,y in [(-1,0), (1,0), (0, -1), (0,1)]:
                if ni+x<m and ni+x>=0 and nj+y<n and nj+y>=0 and not isAtl[ni+x][nj+y]:
                    if heights[ni][nj] <= heights[ni+x][nj+y]:
                        isAtl[ni+x][nj+y] = True
                        atlStack.append((ni+x, nj+y))
        return res