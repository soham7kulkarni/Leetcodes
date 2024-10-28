# Approach - BFS
# TC - O(N)
# SC - O(W) -> O(N/2) -> highest width of tree

from collections import deque  # Import deque from collections for efficient queue operations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Initialize the value of the node
        self.left = left     # Initialize the left child of the node
        self.right = right   # Initialize the right child of the node

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:          # If the tree is empty, return an empty list
            return []
        
        result = []           # Initialize the result list to store levels
        q = deque()          # Create a deque to use as a queue
        q.append(root)       # Add the root node to the deque
        
        while q:             # Continue until the deque is empty
            size = len(q)    # Get the number of nodes at the current level
            li = []          # Initialize a list to store values of the current level
            
            for _ in range(size):  # Iterate through all nodes at the current level
                curr = q.popleft()   # Remove the front node from the deque
                li.append(curr.val)   # Add the value of the current node to the list
                
                if curr.left:        # If the current node has a left child
                    q.append(curr.left)  # Add it to the deque
                if curr.right:       # If the current node has a right child
                    q.append(curr.right)  # Add it to the deque
            
            result.append(li)     # Append the current level's values to the result
        
        return result             # Return the final result containing level order traversal
