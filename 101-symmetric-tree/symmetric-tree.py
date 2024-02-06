# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        self.flag = True
        self.dfs(root.left, root.right)
        return self.flag
    def dfs(self, left, right):
        if left is None and right is None: return
        if left is None or right is None or left.val != right.val:
            self.flag = False
            return
        if self.flag:
            self.dfs(left.left, right.right)
            self.dfs(left.right, right.left)

        