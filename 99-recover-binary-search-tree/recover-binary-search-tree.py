# Approach - We traverse inorder, if we find just 1 breach, its straigh forward swap.
# We might find 2nd breach in other subtree. At that time the incoming root is the main problem.
# Hence we maintain two pointers and update the first node with incoming root.
# In second pointer we maintain the previous. ( The value bigger than root, causing breach)
# At last we swap first with second.

# TC - O(N), SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base
        if root is None: return
        # logic
        self.inorder(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        
    def inorder(self, root):
        # base
        if not root: return
        # logic
        self.inorder(root.left)
        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = root
                self.second = self.prev
            else:
                self.first = root
        self.prev = root
        self.inorder(root.right)

        