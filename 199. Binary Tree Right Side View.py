# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                nd = q.popleft()
                if nd.left: q.append(nd.left)
                if nd.right: q.append(nd.right)
                if i == l-1: res.append(nd.val)
        return res