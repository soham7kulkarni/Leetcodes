# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        # Initialize a variable to keep track of the maximum diameter found so far
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty, the diameter is 0
        if not root:
            return 0
        
        # Calculate the height of the left and right subtrees from the root
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # Update the maximum diameter by comparing with the sum of left and right heights
        self.max = max(self.max, left + right)
        
        # Return the maximum diameter found
        return self.max

    def helper(self, root):
        # Base case: if the node is null, return a height of 0
        if not root:
            return 0
        
        # Recursively find the height of the left subtree
        left = self.helper(root.left)
        
        # Recursively find the height of the right subtree
        right = self.helper(root.right)
        
        # Find the maximum height between the left and right subtree heights
        maxx = max(left, right)
        
        # Update the maximum diameter by considering the sum of the current node's left and right subtree heights
        self.max = max(self.max, left + right)
        
        # Return the height of the current node, which is max(left, right) + 1
        return maxx + 1