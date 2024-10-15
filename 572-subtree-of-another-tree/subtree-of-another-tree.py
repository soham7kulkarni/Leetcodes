# Approach - we match root and subroot and then starts comapring both trees
# It is imp to note that, we can find subroot any where in tree
# Hence we should check with all nodes before start comapring tree and subtree
# TC - O(M,N)
# SC - O(H)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        # This will traverse left of root            this will traverse right of root   
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def is_same_tree(self, root, subroot) -> bool:
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False

        return (root.val == subroot.val) and self.is_same_tree(root.left, subroot.left) and self.is_same_tree(root.right, subroot.right)

        