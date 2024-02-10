# Approach - DFS. Move to left if the root value is greater than low
# Move to right if root value is less than high
# TC - O(n), SC - O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        self.dfs(root, low, high)
        return self.result

    def dfs(self, root, low, high):
        if not root: return
        if root.val >= low and root.val <= high:
            self.result += root.val

        if root.val > low:  self.dfs(root.left, low, high)
       
        if root.val < high: self.dfs(root.right, low ,high)

        return self.result
    
        