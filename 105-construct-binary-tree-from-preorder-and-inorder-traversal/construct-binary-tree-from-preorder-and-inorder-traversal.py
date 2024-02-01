# Approach - We build hashmap on inorder to find root index in O(1). 
# We also use two pointers for maintaining start and end and avoid creating different slice for every subtree.
# At first we find root in preorder. Then we find root index in inorder. We now have left half and right half.
# In these half, we perform recursion for subtrees.
# We hit the leaf when both LHS, RHS nodes are nil. In two pointers, we cross our start and end.
# First we form left half, then right half and then root and then we come out of left subtree and move to left.
# TC - O(N), traversing over preorder array
# SC - O(N), creating hashmap of inorder array


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.map = {val: idx for idx,val in enumerate(inorder)}
        self.idx = 0
        return self.helper(preorder, 0, len(preorder)-1)

    def helper(self, preorder, start, end):
        # base
        if start > end:
            return None
        # logic
        root_val = preorder[self.idx]
        root = TreeNode(root_val)
        self.idx+=1
        root_idx = self.map[root_val]
        root.left = self.helper(preorder, start, root_idx-1)
        root.right = self.helper(preorder, root_idx+1, end)
        return root

        