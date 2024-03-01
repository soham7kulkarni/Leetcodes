# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return self.result
        self.inorder(root, k)
        return self.result

    def inorder(self, root, k):
        if not root: return
        self.inorder(root.left, k)
        self.count += 1
        if root and self.count == k:
            self.result = root.val
            return 
        self.inorder(root.right, k)

        