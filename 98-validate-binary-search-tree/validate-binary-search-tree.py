# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = root
        prev = None
        
        while curr is not None:
            if curr.left is not None:
                pre = curr.left
                while pre.right is not None and pre.right != curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    if prev is not None and prev.val >= curr.val:
                        return False
                    prev = curr
                    curr = curr.right
            else:
                if prev is not None and prev.val >= curr.val:
                    return False
                prev = curr
                curr = curr.right
        
        return True

        