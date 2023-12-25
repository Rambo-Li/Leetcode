class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        net = [[-1]*(n+1) for _ in range(n+1)]
        for time in times:
            x, y, w = time
            net[x][y] = w
        hp = [(0, k)]
        heapq.heapify(hp)
        visited = set()
        res = 0

        while hp and len(visited)<n:
            distance, node = heapq.heappop(hp)
            if node not in visited:
                visited.add(node)
                res = max(res, distance)
                for j in range(1, n+1):
                    if net[node][j]!=-1 and j not in visited:
                        heapq.heappush(hp, (distance+net[node][j], j))
        return res if len(visited)==n else -1

'''
Concept: Shortest path to all nodes. 
DS: A set to keep track of nodes already included.
    A min heap to keep track of nodes connected to visited nodes as a whole.
Algo: Choose the shortest edge to include as next. Note the two nodes of that edge might already be included.
    While loop conditions.
'''