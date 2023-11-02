# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Morris Inorder Traversal
# Find the inorder predecessor 
# from root, go to left if exist or else go to right side of the root
# if left exists, go to first left and then go to right till we find the null for right child. Then link right child with root as it will become inorder predecessor. Then go to left child of the current(root). If we find the right child is already linked then unlink it and go to right child of the curr.

# TC - Amortized(nh) n - number of nodes, h - height
# SC - no stack or recursion calls, in place
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



        