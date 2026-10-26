# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 
            
        def isSameTree(p,q):
            if not p and not q: return True
            if (p and q) and (p.val == q.val):
                l = isSameTree(p.left, q.left)
                r = isSameTree(p.right, q.right)
                return l and r
            else:
                return False 
        
        if isSameTree(root, subRoot):
            return True
        else:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r 