class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        seen = set()
        seen.add((0,0))
        res = 0
        hp = [(grid[0][0], 0, 0)]
        heapq.heapify(hp)
        while hp and (n-1,n-1) not in visited:
            height, x, y = heapq.heappop(hp)
            visited.add((x,y))
            res = max(res, height)
            for d1, d2 in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (x+d1, y+d2) not in seen and x+d1>=0 and x+d1<=n-1 and y+d2>=0 and y+d2<=n-1:
                    seen.add((x+d1, y+d2))
                    heapq.heappush(hp, (grid[x+d1][y+d2], x+d1, y+d2))

        return res

'''
Concept: weighted edge, shortest path. Partition the graph to three parts, visited, connected and don't care.
DS: A set to keep track of visited nodes.
    A min_heap for the frontier. 
    A set to keep track of edges that has been put in the frontier so there is no duplicates. 
Algo: Choose the shortest edge from the frontier to join the visited. And put connected nodes on the frontier. 
    Each node is connected to four adjacent nodes, so duplicates will be in the frontier if we don't filter. It is okay but slow surely.
    While loop condition.
'''