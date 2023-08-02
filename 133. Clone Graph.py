class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        stack = [node]
        while stack:
            nd = stack.pop()
            if nd.val not in visited:
                visited[nd.val] = Node(nd.val)
            # if nd.val == 1:
                root = visited[nd.val]
            ne = []
            for neigh in nd.neighbors:
                if neigh.val not in visited:
                    visited[neigh.val] = Node(neigh.val)
                    stack.append(neigh)
                ne.append(visited[neigh.val])
            visited[nd.val].neighbors = ne
        return root