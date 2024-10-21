#         1
#        / \
#       2   3
#        \   \
#         4   5
#        /   / \
#       6   7   8


# Approach - go to particular node
# If node doesn't exists, return
# If node exists, update the length of zigzag path
# We have already counted the length of zigzap path till that node
# If we are traversing in same direction
# (from 3 to 5, we were moving right and not changing direction, then we set length of zigzap as 1)
# If we are moving in opposite direction, we increase length of zigzap by 1
# Hence, at particular node, we just update the length of longest zigzap pattern globally

# TC - O(N)
# SC - O(H)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.


class Solution:
    def __init__(self):
        # Initialize the maximum ZigZag length
        self.max_zigzag = 0
    
    # Helper function for DFS traversal (as a class method)
    def dfs(self, node, direction, length):
        if not node:
            return
        
        # Update the maximum ZigZag length if necessary
        self.max_zigzag = max(self.max_zigzag, length)
        
        # If the last move was to the left, now go right
        if direction == 0:
            # Continue the zigzag by moving to the right
            self.dfs(node.right, 1, length + 1)
            # Start a new zigzag path by moving to the left
            self.dfs(node.left, 0, 1)
        else:
            # Continue the zigzag by moving to the left
            self.dfs(node.left, 0, length + 1)
            # Start a new zigzag path by moving to the right
            self.dfs(node.right, 1, 1)
    
    def longestZigZag(self, root: TreeNode) -> int:
        # Start DFS from the root: Try both directions
        if root.left:
            self.dfs(root.left, 0, 1)  # Start by moving left
        if root.right:
            self.dfs(root.right, 1, 1) # Start by moving right
        
        return self.max_zigzag
