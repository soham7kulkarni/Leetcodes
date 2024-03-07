# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depthX, depthY = 0,0
    parentX, parentY = None, None
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        self.helper(root, x, y, 0, None)
        if self.depthX == self.depthY and self.parentX != self.parentY: return True
        return False
    
    def helper(self, root, x, y, depth, parent):
        # logic
        if not root: return
        # logic
        if root.val == x:
            self.depthX = depth
            self.parentX = parent
        if root.val == y:
            self.depthY = depth
            self.parentY = parent
        if self.parentX == None or self.parentY == None:
            self.helper(root.left, x, y, depth+1, root)
        if self.parentX == None or self.parentY == None:
            self.helper(root.right, x, y, depth+1, root)
        

        