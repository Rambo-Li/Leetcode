class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        maxdist = [[0]*n for _ in range(m)]
        def dps(x,y):
            if maxdist[x][y]:
                return maxdist[x][y]

            ans = 1
            for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0<=x+dx<m and 0<=y+dy<n and matrix[x+dx][y+dy]>matrix[x][y]:
                    ans = max(ans, dps(x+dx, y+dy)+1)

            maxdist[x][y] = ans
            return ans

        return max([dps(a,b) for a in range(m) for b in range(n)])
    
'''
Concept: a node's value is fixed only after all pathes into have been considered, this is different from typical DFS or BFS.
    Either uses a DFS on all incoming edges, or a BFS with indgree(0 indegree means starting node, -1 indegree from each iteration)
DS: a memory matrix for each node, or an indegree matrix for indegrees
Algo: DFS+memo, indegree pops a batch and update the indegree and any 0 indegree goes into the next batch
'''