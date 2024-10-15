class Solution:
    def __init__(self):
        self.count = 0  # Initialize count of visited nodes
        self.result = 0  # Initialize result to store the k-th smallest value
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)  # Start in-order traversal
        return self.result  # Return the k-th smallest value

    def inorder(self, root, k) -> None:
        if not root:  # Base case: if the node is None, return
            return
        
        self.inorder(root.left, k)  # Traverse left subtree
        
        self.count += 1  # Increment the count of visited nodes
        if self.count == k:  # Check if we've reached the k-th smallest
            self.result = root.val  # Update result with the current node's value
            return  # Exit the traversal early since we found the k-th smallest
        
        self.inorder(root.right, k)  # Traverse right subtree
