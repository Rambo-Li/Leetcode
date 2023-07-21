class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while True:
            if p.val< curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


#         stack = []
#         stack.append(root)
#         arr = []
#         while stack:
#             r = 0
#             node = stack.pop()
#             if node == p: parent1 = arr.copy()+[(node, 1)]
#             if node == q: parent2 = arr.copy()+[(node, 1)]
#             if arr:
#                 nd, child = arr.pop()
#                 assert nd.left == node or nd.right == node
#                 child -= 1
#                 if child>0 or (nd == root and child==0):
#                     arr.append((nd, child))
            
#             if node.left != None: 
#                 stack.append(node.left)
#                 r += 1
#             if node.right != None: 
#                 stack.append(node.right)
#                 r += 1
#             if r >0: arr.append((node, r))

#         print(parent1)
#         print(parent2)
#         l = min(len(parent1), len(parent2))
#         for k in range(l):
#             if parent1[k][0] != parent2[k][0]:
#                 return parent1[k-1][0]
#         return parent1[l-1][0]

""" I thought it was a binary tree, setting up an array to hold the parents while dfs. The problem is when to pop node from the parent array. TODO"""