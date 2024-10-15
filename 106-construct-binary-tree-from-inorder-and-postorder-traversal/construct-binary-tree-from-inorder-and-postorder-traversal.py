# Time Complexity: 
# \U0001d442(\U0001d441)
# Space Complexity: 
# \U0001d442(\U0001d441)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.map = {val:idx for idx,val in enumerate(inorder)}

        self.idx = len(postorder)-1
        return self.helper(0, len(inorder) - 1, postorder)
    def helper(self, start, end, postorder) -> None:
        if start > end:
            return None
        rootval = postorder[self.idx]
        root = TreeNode(rootval)
        self.idx -= 1
        rootIdx = self.map[rootval]
        root.right = self.helper(rootIdx + 1, end, postorder)
        root.left = self.helper(start, rootIdx - 1, postorder)
        return root



        