# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pathP = []
        self.pathQ = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.backtrack(root, p, q, path)
        for i in range(len(self.pathP)):
            if self.pathP[i] != self.pathQ[i]:
                return self.pathP[i-1]

        return None

    def backtrack(self, root, p, q, path):
        if not root: return
        path.append(root)
        if root == p:
            self.pathP = path[:]
            self.pathP.append(root)
        if root == q:
            self.pathQ = path[:]
            self.pathQ.append(root)

        self.backtrack(root.left, p, q, path.copy())
        self.backtrack(root.right, p, q, path.copy())

        path.pop()
        