class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = [i for i in range(len(edges)+1)]
        def root(node):
            p = node
            while union[p] != p:
                p = union[p]
            union[node] = p
            return p
        def connect(n1, n2):
            p1 = root(n1)
            p2 = root(n2)
            if p1 == p2:
                return False
            else:
                union[p1] = p2
        for n1, n2 in edges:
            if connect(n1, n2) == False:
                return [n1,n2]
    
# The genius part of union-find algorithm is to use a number represent all connected nodes. When union happens, update one node's number to the other, so the other becomes
# root. 