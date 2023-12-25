class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        hq = [(0, 0)]
        heapq.heapify(hq)
        visited = set()
        res = 0
        while len(visited) < len(points):
            distance, node = heapq.heappop(hq)
            if node not in visited:
                res += distance
                visited.add(node)
                for i in range(len(points)):
                    if i not in visited:
                        heapq.heappush(hq, (abs(points[node][0]-points[i][0])+abs(points[node][1]-points[i][1]), i))

        return res

'''
Concept: Minimum spanning tree. Shortest edges to connect all nodes. 
DS: A set to keep track of already-included nodes.
    A min heap to keep track of nodes that are connected, and choose next node to include.
Algo: Start with the shortest edge. View all included nodes as a whole. Then choose next shortest edge to include.
    Note the two nodes of next shortest edge might be already included.
'''