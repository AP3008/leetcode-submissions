# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Recursive
        # res = []
        # def dfs(node):
        #    if not node:
        #        return None
        #    dfs(node.left)
        #    res.append(node.val)
        #    dfs(node.right)
        # dfs(root)
        # return res 

        # Iterative sol. 

        stack = [] # init stack to keep track of nodes
        if root: # if we have a node as root we add it to the stack 
            stack.append((root, False))
        res = [] # our list of resulting values in order 
        while stack: # while the stack is not empty we want to loop
            node, visited = stack.pop() # remove the element most recently 
            if not visited: # If we have not explored this node we enter this block 
                if node.right: # If the right node is not empty 
                    stack.append((node.right, False)) # we add it to the stack 
                stack.append((node, True)) # mark the current node as explored and put it at the end 
                if node.left: # if the left node is not null 
                    stack.append((node.left, False)) # we add it to the list to be explored after the right side is seen 
            else: # if we have a node in the stack that has been explored 
                res.append(node.val) # we add the value to the list 
        return res 