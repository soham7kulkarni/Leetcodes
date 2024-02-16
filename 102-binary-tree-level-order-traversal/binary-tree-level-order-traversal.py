# Approach - DFS
# depth == size, True: there no exist any node for particular depth. 
# Create one list and append
# False: Already nodes are present at that depth level(processed). Just append
# TC - O(N)
# SC - O(H) Stack of recursive calls

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return self.result
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, depth):
        if not root: return
        if depth == len(self.result):
            self.result.append([])
        self.result[depth].append(root.val)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        