class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {}
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            d[pre] = d.get(pre, []) + [course]
            indegree[course] += 1
        q = deque([pre for pre in range(numCourses) if indegree[pre]==0])
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            if course in d:
                for cou in d[course]:
                    indegree[cou] -= 1
                    if indegree[cou] == 0:
                        q.append(cou)
        return res if len(res) == numCourses else []