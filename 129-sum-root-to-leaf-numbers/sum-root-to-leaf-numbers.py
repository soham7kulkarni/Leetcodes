# Approach - int based preorder
# children passing values to root
# root having left sum and right sum
# root returning sum of both ends
# TC - O(N)
# SC - O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.helper(root, 0)
    def helper(self, root, currNum) -> int:
        # base
        if not root: return 0
        # logic
        currNum = currNum*10 + root.val
        if not root.left and not root.right:
            return currNum
        left = self.helper(root.left, currNum)
        
        right = self.helper(root.right, currNum)

        return left + right
        