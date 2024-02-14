# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: 
            return result
        self.dfs(root, 0, result)
        return result
    
    def dfs(self, root, depth, result):
        if not root: 
            return
        if depth == len(result) : result.append(root.val)
        self.dfs(root.right, depth + 1, result)  # Visit right child first
        self.dfs(root.left, depth + 1, result)   # Then visit left child


        