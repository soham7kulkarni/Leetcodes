# Approach - DFS
# TC - O(N)
# SC - O(H), in worst case, skew tree, O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.dfs(root, 1)
        return self.max_depth
    def dfs(self, root, depth):
        if not root:
            return
        self.dfs(root.left, depth+1)
        if not root.left and not root.right:
            self.max_depth = max(self.max_depth, depth)
            return
        self.dfs(root.right, depth+1)
        