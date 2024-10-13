# Approach - void based inorder
# TC - O(N)
# SC - O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.currSum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.helper(root, 0)
        return self.currSum
    def helper(self, root, currNum) -> None:
        # base
        if not root: return
        # logic
        currNum = currNum*10 + root.val
        self.helper(root.left, currNum)
        if not root.left and not root.right:
            self.currSum += currNum
            return
        self.helper(root.right, currNum)
        