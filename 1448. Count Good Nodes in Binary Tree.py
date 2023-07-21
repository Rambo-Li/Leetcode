# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        q = deque()
        q.append(root)
        while q:
            nd = q.popleft()
            if nd.left:
                if nd.left.val >= nd.val:
                    res += 1
                nd.left.val = max(nd.val, nd.left.val)
                q.append(nd.left)
            if nd.right:
                if nd.right.val >= nd.val:
                    res += 1
                nd.right.val = max(nd.val, nd.right.val)
                q.append(nd.right)
        return res