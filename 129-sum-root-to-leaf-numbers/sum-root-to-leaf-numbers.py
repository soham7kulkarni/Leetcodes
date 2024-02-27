# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return self.result
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, num):
        # base
        if not root: return
        # logic
        num = num*10 + root.val
        if root.left is None and root.right is None: self.result += num
        self.dfs(root.left, num)
        self.dfs(root.right, num)



        