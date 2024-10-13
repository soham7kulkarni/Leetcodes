# TC - O(N)
# SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
        self.prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.flag
    def inorder(self, root) -> None:
        if not root: return
        self.inorder(root.left)
        if self.prev and self.prev.val >= root.val:
            self.flag = False
            return
        self.prev = root
        self.inorder(root.right)

            

        