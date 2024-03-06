# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        self.dfs(root, 0, result)
        return result

    def dfs(self, root, depth, result):
        # base
        if not root: return
        # logic
        if depth == len(result):
            result.append(root.val)
        else:
            result[depth] = root.val
        # left
        self.dfs(root.left, depth + 1, result)
        # right
        self.dfs(root.right, depth + 1, result)


        