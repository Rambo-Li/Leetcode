# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def maxPathGain(root):
            nonlocal res
            if not root:
                return 0

            leftgain = max(maxPathGain(root.left), 0)
            rightgain = max(maxPathGain(root.right), 0)
            currentmax = leftgain+rightgain+root.val
            res = max(res, currentmax)

            return root.val + max(leftgain, rightgain)
        
        maxPathGain(root)
        return res

# recursive function returns the max path going upwards, meanwhile, updating the left+root+right value. For any subpart of the tree, the value 
# is updated as left+root+right along the recursion.