# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        left = self.depth(root.left)
        right = self.depth(root.right)
        res = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        res = max(res, left + right)
        return res

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

# Diameter is max of (diameter of left, diameter of right, depth of left depth of right). The best solution puts the max operation in the recursion.
# The genius part is the max can be two scenarios, when the tree is small, it is only one scenario, that's why you can put the max in the recursion.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(root):
            if not root:
                return 0
            nonlocal res
            left = depth(root.left)
            right = depth(root.right)
            res = max(res, left+right)
            return 1 + max(left, right)
        
        depth(root)
        return res