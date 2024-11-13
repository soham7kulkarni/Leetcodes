# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max = max(self.max, left + right)
        return self.max
    def helper(self, root):
        # base
        if not root:
            return 0
        # logic
        left = self.helper(root.left)
        right = self.helper(root.right)
        maxx = max(left, right)
        self.max = max(self.max, left + right)
        return maxx + 1


        
        

        