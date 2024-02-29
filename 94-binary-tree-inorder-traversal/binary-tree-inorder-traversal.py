# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return self.result
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if root:
            self.result.append(root.val)
        self.inorder(root.right)



        