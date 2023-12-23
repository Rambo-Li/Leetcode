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