# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depthX = 0
    depthY = 0
    parentX = None
    parentY = None
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root, x, y, 0, None)
        if self.parentX != self.parentY and self.depthX == self.depthY: return True
        return False
    
    def dfs(self, root, x, y, depth, parent):
        # base
        if not root: return

        # logic

        # x
        if root.val == x:
            self.parentX = parent
            self.depthX = depth
        # y
        if root.val == y:
            self.parentY = parent
            self.depthY = depth

        # optimize
        if self.parentX is None or self.parentY is None:
            self.dfs(root.left, x, y, depth+1, root)
        if self.parentX is None or self.parentY is None:
            self.dfs(root.right, x, y, depth+1, root)
        
        