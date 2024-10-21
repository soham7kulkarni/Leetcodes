# Approach - DFS exploring all paths
# As we process the current node, we compare it with root.
# If current node is equal or greater then only we should proceed ahead
# We can collect number of good nodes at each node from left nd right
# We should update max good nodes value everytime we collect new good node

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
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform DFS and count good nodes
        def dfs(node, max_so_far):
            # Base case: If the node is None, return 0 (no good node here)
            if not node:
                return 0
            
            # Check if the current node is a "good" node
            good = 1 if node.val >= max_so_far else 0
            
            # Update the max_so_far to be the maximum of current node's value or previous max
            new_max = max(max_so_far, node.val)
            
            # Recur on left and right children and count the good nodes in each subtree
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            
            # Return the total count of good nodes from this subtree
            return good
        
        # Start the DFS with the root node, and the initial max_so_far is the value of the root
        return dfs(root, root.val)

        