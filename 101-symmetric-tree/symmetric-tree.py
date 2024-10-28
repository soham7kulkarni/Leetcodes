# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Initialize the value of the node
        self.left = left     # Initialize the left child of the node
        self.right = right   # Initialize the right child of the node

class Solution:
    def __init__(self):
        self.flag = True      # A flag to track if the tree is symmetric

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:           # If the tree is empty, it is symmetric
            return True
        self.helper(root.left, root.right)  # Start the recursive symmetry check
        return self.flag      # Return the value of flag indicating symmetry

    def helper(self, left, right):
        if not left and not right:  # If both nodes are None, they are symmetric
            return
        if not left or not right or left.val != right.val:  # Check if nodes are not equal or one is None
            self.flag = False        # Set flag to False if asymmetric condition is met
            return
        if self.flag:               # Only proceed if the tree is still symmetric
            self.helper(left.left, right.right)  # Check outer children
        if self.flag:               # Only proceed if the tree is still symmetric
            self.helper(left.right, right.left)  # Check inner children
