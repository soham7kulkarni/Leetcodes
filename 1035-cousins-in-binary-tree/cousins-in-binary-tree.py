# Approach 1 (DFS) - traverse the tree and when we find x, record the depth and parent. Same for y.
# At the end, check if depth of both x and y is same and parents are different.
# We can stop left and right traversing if we find parents of both (Optimization)
# TC - O(N), SC - O(H)

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
        if not root: return False
        self.dfs(root, x, y, 0, None)
        return self.parentX != self.parentY and self.depthX == self.depthY
    def dfs(self, root, x, y, depth, parent):
        # base
        if not root: return
        # logic
        if root.val == x:
            self.depthX = depth
            self.parentX = parent
        if root.val == y:
            self.depthY = depth
            self.parentY = parent
        if self.parentX == None or self.parentY == None:
            self.dfs(root.left, x, y, depth+1, root)
        if self.parentX == None or self.parentY == None:
            self.dfs(root.right, x, y, depth+1, root)

        

        