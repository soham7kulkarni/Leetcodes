# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base
        if root is None or p is None or q is None: return root
        # Recursive logic
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if root == p or root == q:
            return root
        if left is None and right is None:
            return None
        elif left is not None and right is None:
            return left
        elif left is None and right is not None:
            return right
        else:
            return root

        