# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = collections.deque([root]) 
        levels = [[root.val]]
        temp = deque() 
        while queue:
            node = queue.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)

            if not queue: 
                if temp:
                    levels.append([n.val for n in temp])
                queue = temp
                temp = deque() 
        return levels 

            
             