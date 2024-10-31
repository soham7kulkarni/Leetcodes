# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # A helper function that returns the height of the tree if balanced, or -1 if unbalanced.
        def height(node):
            if not node:
                return 0  # A null tree has a height of 0
            left_height = height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
            right_height = height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            return max(left_height, right_height) + 1
        
        # The tree is balanced if height does not return -1
        return height(root) != -1
        