# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.result = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root): 
            if not root or self.result is not None:
                return
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return

            inorder(root.right)


        inorder(root)
        return self.result

        
        


        