# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mapp = {val: idx for idx, val in enumerate(inorder)}
        self.index = 0
        return self.helper(preorder, 0, len(preorder)-1)

    def helper(self, preorder, start, end):
        if start > end:
            return None
        root_val = preorder[self.index]
        root = TreeNode(root_val)
        root_idx = self.mapp[root_val]
        self.index += 1
        root.left = self.helper(preorder, start, root_idx-1)
        root.right = self.helper(preorder, root_idx+1, end)
        return root