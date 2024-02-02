# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.flag = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.flag
    def helper(self, root: Optional[TreeNode]):
        if not root : return
        self.helper(root.left)
        if self.prev is not None and self.prev.val >= root.val:
            self.flag = False
        self.prev = root
        self.helper(root.right)
        