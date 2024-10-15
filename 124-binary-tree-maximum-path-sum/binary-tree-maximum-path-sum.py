# Approach - for a particular node,
# we calculate left sum and right sum.
# We add these two with node.val so that its a path value
# considering node as a part of path
# Then we update global sum as its not necessary
# that path should traverse from root. Root can be excluded.
# Then we send sum upward from that node to their parent,
# we should consider only one branch. hence we consider max of 
# left_sum and right_sum and node.val to it an push it to root
# TC - O(N)
# SC - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_sum
    def dfs(self, root) -> None:
        if not root:
            return 0
        left_sum = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))

        curr_sum = root.val + left_sum + right_sum
        self.max_sum = max(self.max_sum , curr_sum)

        return root.val + max(left_sum, right_sum)

        