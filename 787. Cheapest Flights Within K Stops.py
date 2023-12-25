class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        net = [[-1]*n for _ in range(n)]
        for flight in flights:
            net[flight[0]][flight[1]] = flight[2]

        distance = [inf]*n
        distance[src] = 0
        frontier = [src]

        while k>=0:
            temp = []
            temp_distance = distance[:]
            while frontier:
                fr = frontier.pop()
                for to, dist in enumerate(net[fr]):
                    if dist != -1 and temp_distance[to] > distance[fr]+dist:
                        temp.append(to)
                        temp_distance[to] = distance[fr]+dist

            frontier = temp[:]
            distance = temp_distance[:]
            k -= 1
        return distance[dst] if distance[dst] != inf else -1
    
'''
Concept: BFS within K steps. Or Bellman Ford for shortest path.
DS: BFS uses a queue, but K steps requires seperation of layers so an extra count variable or temp array is needed.
    A array to keep the result. The array might be updated more than once per iteration, if the from and to are both updated, 
    then the distance is actually not achievable. So a temp array is needed to make sure the from is always from last iteration.
Algo: BFS, only put distance-changed nodes on the queue. Use last iteration 'from' and this iteration 'to' to determine if distance changed.
'''      