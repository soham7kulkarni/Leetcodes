# TC - O(N)
# SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a mapping from value to its index in the inorder list
        self.map = {value: idx for idx, value in enumerate(inorder)}
        # Initialize the index for the current root in the preorder list
        self.idx = 0
        # Start the recursive tree construction from the entire range of inorder
        return self.helper(0, len(inorder) - 1, preorder)  # Return the constructed tree

    def helper(self, start, end, preorder) -> TreeNode:
        # Base case: if the current range is invalid, return None
        if start > end:
            return None
        # Get the current root value from preorder using the current index
        rootVal = preorder[self.idx]
        # Create the root node with the current root value
        root = TreeNode(rootVal)
        # Increment the index for the next root in preorder
        self.idx += 1
        # Find the index of the current root in inorder
        rootIdx = self.map[rootVal]
        # Recursively build the left subtree (left part of inorder)
        root.left = self.helper(start, rootIdx - 1, preorder)
        # Recursively build the right subtree (right part of inorder)
        root.right = self.helper(rootIdx + 1, end, preorder)
        # Return the constructed root node
        return root
