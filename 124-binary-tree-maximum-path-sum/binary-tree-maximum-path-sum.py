# Approach - for a particular node,
# we calculate left sum and right sum.
# We add these two with node.val so that its a path value
# considering node as a part of path
# Then we update global sum as its not necessary
# that path should traverse from root. Root can be excluded.
# Then we send sum upward from that node to their parent,
# we should consider only one branch. hence we consider max of 
# left_sum and right_sum and node.val to it an push it to root
# TC - O(N)
# SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        # Initialize max_sum to the smallest possible value
        self.max_sum = float('-inf')  # This will hold the maximum path sum found

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # This method is the entry point to calculate the maximum path sum
        self.dfs(root)  # Start the depth-first search from the root
        return self.max_sum  # Return the maximum path sum found

    def dfs(self, root) -> None:
        # Depth-first search method to calculate maximum path sum
        if not root:
            return 0  # If the node is null, return 0 (base case)

        # Recursively get the maximum path sum from the left child
        left_sum = max(0, self.dfs(root.left))  
        # We use max(0, ...) to ignore negative sums (we only consider positive contributions)

        # Recursively get the maximum path sum from the right child
        right_sum = max(0, self.dfs(root.right))  

        # Calculate the current path sum including the current node
        curr_sum = root.val + left_sum + right_sum  
        # Update the maximum path sum found so far
        self.max_sum = max(self.max_sum, curr_sum)  

        # Return the maximum path sum extending to the parent node
        return root.val + max(left_sum, right_sum)  
        # We return the value of the current node plus the maximum of the left or right child sums


        