# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        stack = []
        stack.append(root)
        while stack:
            nd = stack.pop()
            while arr and nd.val > arr[-1].val:
                temp = arr.pop()
                k -= 1
                if k == 0: return temp.val
            if nd.left and nd.right:
                stack.append(nd.right)
                stack.append(nd.left)
                arr.append(nd)
            elif nd.right:
                k -= 1 
                stack.append(nd.right)
            elif nd.left:
                stack.append(nd.left)
                arr.append(nd)
            else:
                k -= 1
            if k == 0:
                return nd.val
        while arr:
            temp = arr.pop()
            k -= 1
            if k == 0: return temp.val

# best solution:
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
# This is how to traverse BST in order. Stack append all left nodes, then pop and do it again.