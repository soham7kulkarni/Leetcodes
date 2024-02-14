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
        
        self.dfs(root, 0, None, x, y)
        if self.depthX == self.depthY and self.parentX != self.parentY: return True
        return False
        
    def dfs(self, root, depth, parent, x, y):
        if not root: return
        if root.val == x:
            self.parentX = parent
            self.depthX = depth
        if root.val == y:
            self.parentY = parent
            self.depthY = depth
        if self.parentX is None or self.parentY is None:
            self.dfs(root.left, depth+1, root, x, y)
        if self.parentX is None or self.parentY is None:
            self.dfs(root.right, depth+1, root, x, y)
