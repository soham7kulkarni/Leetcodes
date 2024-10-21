# Approach - DFS
# TC - O(N)
# SC - O(H), in worst case, skew tree, O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        # Initialize the max_depth variable to 0, which will store the maximum depth of the tree.
        self.max_depth = 0
    
    # This method is called to find the maximum depth of the binary tree.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the root is None (i.e., the tree is empty), return 0 because there is no depth.
        if not root: 
            return 0
        
        # Start depth-first search (DFS) traversal from the root with an initial depth of 1.
        self.dfs(root, 1)
        
        # After the DFS traversal, return the maximum depth found.
        return self.max_depth
    
    # Helper method to perform DFS and calculate the depth.
    def dfs(self, root, depth):
        # If the current node is None, return (base case for recursion).
        if not root:
            return
        
        # Recursively traverse the left subtree, increasing the depth by 1.
        self.dfs(root.left, depth + 1)
        
        # If the current node is a leaf node (i.e., both left and right children are None),
        # update the maximum depth encountered so far.
        if not root.left and not root.right:
            # Update max_depth to the greater of current max_depth and the depth of this leaf node.
            self.max_depth = max(self.max_depth, depth)
            return
        
        # Recursively traverse the right subtree, increasing the depth by 1.
        self.dfs(root.right, depth + 1)
