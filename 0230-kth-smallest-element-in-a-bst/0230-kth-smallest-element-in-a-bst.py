# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # Just go down left keeping track of the values they're appending, if the q is less than 

        q = deque() 
        def populateQ(node):
            if node.left:
                populateQ(node.left)
            q.append(node.val)
            print(node.val)
            if node.right:
                populateQ(node.right)
        
        populateQ(root)

        if len(q) <= k: return q[-1]
        res = 0
        while k > 0 and q:
            res = q.popleft()
            k-=1
        return res
            

