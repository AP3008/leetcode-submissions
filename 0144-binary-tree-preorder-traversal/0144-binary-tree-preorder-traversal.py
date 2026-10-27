# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
       # Recrusive sol. 
       # res = []
       # def dfs(node):
       #     if not node:
       #         return None
       #     res.append(node.val)
       #     dfs(node.left)
       #     dfs(node.right)
       # dfs(root)
       # return res 

       # Iterative sol. 
        stack = [] 
        if root:
            stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            res.append(node.val)
        return res