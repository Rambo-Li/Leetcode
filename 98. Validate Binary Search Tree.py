# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True

        def isBST(root, lValue, rValue):
            if not root:
                return True
            if root.val >= rValue or root.val <= lValue: return False
            # if root.left and root.left.val >= root.val: return False
            # if root.right and root.right.val <= root.val: return False
            return isBST(root.left, lValue, root.val) and isBST(root.right, root.val, rValue)

        return isBST(root, float("-inf"), float("inf")) 
    
# The key of BST if each node is within a range set by its ancestors.