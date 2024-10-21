# TC - O(H)
# SC - O(H)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the current root is None, we've reached a dead end, return None
        if not root:
            return None
        
        # If we found the node with the value equal to val, return this node
        if root.val == val:
            return root
        
        # If val is less than the current node's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is greater than the current node's value, search in the right subtree
        return self.searchBST(root.right, val)
        