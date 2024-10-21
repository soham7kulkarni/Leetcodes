# Approach - DFS:root - right - left
# We check the length of array.If it equal to depth then we add node to array
# It means we are adding most right element to array.
# At root, array = [], depth = 0
# After root.right, array = [root.val], depth = 1 (matches! hence adding root.right to array)

# TC - O(N)
# SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # Initialize an empty list to store the right-side view
        if not root:
            return result  # If the root is None, return an empty list
        
        # Call the helper function to perform DFS (depth-first search)
        self.dfs(root, 0, result)
        
        return result  # Return the final result after DFS traversal
    
    # Helper function to perform depth-first search (DFS)
    def dfs(self, root, depth, result):
        if not root:
            return  # Base case: if the current node is None, return
        
        # If this is the first node at the current depth, add it to the result
        if depth == len(result):
            result.append(root.val)
        
        # Visit the right child first, ensuring we see the rightmost node at each level
        self.dfs(root.right, depth + 1, result)
        
        # Then visit the left child (in case there are no right children at this depth)
        self.dfs(root.left, depth + 1, result)
        