class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            d[pre] = d.get(pre, []) + [course]
            indegree[course] += 1
            
        q = deque([pre for pre in range(numCourses) if indegree[pre] == 0])
        res = 0
        while q:
            pre = q.popleft()
            res += 1
            if pre in d:
                for course in d[pre]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
        return res == numCourses
    
# This is a DAG cycle finding problem. A child goes back to any of its parent consists of a cycle, which means the call to child needs to contain all ancestors' information.
# Or to use a golbal data structure like in backtracking. 
# This indegree algorithm starts with all roots(no incoming edges), and deduct a node's indegree per visit. If there is a cycle, then some nodes will have edges that can't be
# visited through root, their indegree will be >=1. 