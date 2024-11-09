# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != -1
    def helper(self, root) -> int:
        # Base case: if the current node is None, its height is 0
        if not root:
            return 0
        
        # Recursively calculate the height of the left subtree
        left_height = self.helper(root.left)
        # If left subtree is unbalanced, propagate the imbalance (-1) up the call stack
        if left_height == -1:
            return -1
        
        # Recursively calculate the height of the right subtree
        right_height = self.helper(root.right)
        # If right subtree is unbalanced, propagate the imbalance (-1) up the call stack
        if right_height == -1:
            return -1
        
        # Check if the current node is balanced by comparing left and right subtree heights
        if abs(left_height - right_height) > 1:
            # Return -1 to indicate imbalance
            return -1
        
        # If balanced, return the height of the current node as max height of subtrees + 1
        return max(left_height, right_height) + 1

        