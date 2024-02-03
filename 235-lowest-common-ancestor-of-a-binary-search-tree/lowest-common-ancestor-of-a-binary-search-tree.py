# Approach - Both P and Q less, go to left. Both are great, go to right. If found root, return root. 
# If we found P and Q on LHS and RHS o root, return root.
# TC - O(H), SC - O(H)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val: return self.lowestCommonAncestor(root.left, p , q)
        elif root.val < p.val and root.val < q.val: return self.lowestCommonAncestor(root.right, p, q)
        else: return root
        