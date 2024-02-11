# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        return self.dfs(root, low ,high)

    def dfs(self, root, low, high) -> int:
        if not root: return 0
        current = 0
        if root.val >= low and root.val <= high:
           current = root.val
        
        left = self.dfs(root.left, low, high)
        right = self.dfs(root.right, low, high)

        return current+left+right

        