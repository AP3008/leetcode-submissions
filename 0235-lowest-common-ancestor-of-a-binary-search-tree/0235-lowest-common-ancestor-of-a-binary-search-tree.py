# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The root of the subtree where the two nodes split is the lowest common ancestor 
        # Since this is a BST we can just look for the node where they go in two seperate directions is. 

        if not root: return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root