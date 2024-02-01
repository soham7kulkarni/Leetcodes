# Int based recursion
# TC - O(n)
# SC - O(h) - O(N) when skewed
# Approach - For every root(node), calculate LHS and RHS sum and then add it. When we hit the leaf, stop the number formation and just return the formed number.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.currSum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, root: Optional[TreeNode], currNum: int) -> int:

        # base
        if root is None: return 0

        # logic
        currNum = currNum*10 + root.val
        
        left = self.helper(root.left, currNum)
        # st.pop()
        if root.left is None and root.right is None: return currNum
        right = self.helper(root.right, currNum)
        # st.pop()
        return left + right
        
        