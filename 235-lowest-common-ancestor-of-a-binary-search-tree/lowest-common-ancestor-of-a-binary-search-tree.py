# TC - O(N)
# SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If the current node is None, we return None (base case)
        if not root:
            return None
        
        # If either p or q is the root, then root is the LCA
        if root.val == p.val or root.val == q.val:
            return root
        
        # If p and q are on either side of the root, then root is the LCA
        if (p.val < root.val < q.val) or (q.val < root.val < p.val):
            return root
        
        # If both p and q are on the left side
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both p and q are on the right side
        return self.lowestCommonAncestor(root.right, p, q)

        