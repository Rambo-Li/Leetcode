# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        depth = 0
        while stack:
            nd, level = stack.pop()
            depth = max(depth, level)
            if nd.left: stack.append((nd.left, level+1)) 
            if nd.right: stack.append((nd.right, level+1)) 
        return depth
    
# The recursive writing "return 1+max(maxDepth(root.left), maxDepth(root.right))" is so succinct.