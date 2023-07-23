# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            if temp:
                res.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)
            else:
                res.append("N")
        while res and res[-1] == "N":
            res.pop()

        return ",".join(str(i) for i in res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(",")

        leaf = list(map(lambda x: TreeNode(int(x)) if x!= 'N' else None, values))
        root = leaf[0]
        j = 0
        for i in range(len(leaf)):
            if leaf[i]:
                if j+1 < len(leaf):
                    j += 1
                    leaf[i].left = leaf[j]                    
                else:
                    leaf[i].left = None
                
                if j+1 < len(leaf):
                    j += 1
                    leaf[i].right = leaf[j]                    
                else:
                    leaf[i].right = None
        return root