# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.helper(root, 1)
        return self.max_depth
    def helper(self, root, depth):
        if not root:
            return
        self.helper(root.left, depth + 1)
        self.max_depth = max(self.max_depth, depth)
        self.helper(root.right, depth + 1)
            
        