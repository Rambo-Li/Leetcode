# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque()
        q.append((root, 1))
        while q:
            nd, level = q.popleft()
            if len(res) < level:
                res.append([nd.val])
            else:
                res[-1].append(nd.val)
            if nd.left: q.append((nd.left, level+1))
            if nd.right: q.append((nd.right, level+1))
        return res