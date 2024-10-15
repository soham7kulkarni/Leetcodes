# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a mapping from value to its index in the inorder list
        self.map = {val: idx for idx, val in enumerate(inorder)}
        # Initialize the index for the last element in postorder
        self.idx = len(postorder) - 1
        # Start the recursive tree construction from the entire range of inorder
        return self.helper(0, len(inorder) - 1, postorder)

    def helper(self, start, end, postorder) -> TreeNode:
        # Base case: if the current range is invalid, return None
        if start > end:
            return None
        # Get the current root value from postorder using the index
        rootVal = postorder[self.idx]
        # Create the root node with the current root value
        root = TreeNode(rootVal)
        # Decrement the index for the next root in postorder
        self.idx -= 1
        # Find the index of the current root in inorder
        rootIdx = self.map[rootVal]
        
        # Recursively build the right subtree (right part of inorder)
        root.right = self.helper(rootIdx + 1, end, postorder)
        # Recursively build the left subtree (left part of inorder)
        root.left = self.helper(start, rootIdx - 1, postorder)
        
        # Return the constructed root node
        return root
