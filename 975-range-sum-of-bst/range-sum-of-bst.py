# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        while not root: return self.result
        self.helper(root, low, high)
        return self.result

    def helper(self, root, low , high):
        # base
        if not root: return
        # logic
        self.helper(root.left, low, high)
        if low <= root.val <= high:
            self.result += root.val
        self.helper(root.right, low , high)
        
        