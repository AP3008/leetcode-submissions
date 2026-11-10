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
        # Preorder traversal 
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # We have the string in preorder root -> left -> right
        values = data.split(",")
        if values[0] == "N": return None 
        self.i = 0
        def dfs():
            if self.i >= len(values): return None
            if values[self.i] == "N":
                self.i+=1 
                return None
            node = TreeNode(values[self.i])
            self.i+=1 
            node.left = dfs()
            node.right = dfs()
            return node 
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))