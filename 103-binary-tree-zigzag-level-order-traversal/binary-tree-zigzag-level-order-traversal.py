# TC - O(N)
# SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque  # Importing deque for efficient queue operations

class Solution:  # Define the Solution class
    def zigzagLevelOrder(self, root):  # Define the method for zigzag traversal
        if not root:  # Check if the tree is empty
            return []

        result = []  # Initialize the result list
        queue = deque([root])  # Initialize the queue with the root node
        left_to_right = True  # Boolean flag to determine the direction of traversal

        while queue:  # Continue until the queue is empty
            level_size = len(queue)  # Get the number of nodes at the current level
            current_level = deque()  # Initialize a deque to hold current level values
            
            for _ in range(level_size):  # Iterate over the current level
                node = queue.popleft()  # Remove the front node from the queue
                
                # Add the node value to the current level based on the direction
                if left_to_right:
                    current_level.append(node.val)  # Append to the right end
                else:
                    current_level.appendleft(node.val)  # Append to the left end
                
                if node.left:  # If the left child exists, add it to the queue
                    queue.append(node.left)
                if node.right:  # If the right child exists, add it to the queue
                    queue.append(node.right)

            result.append(list(current_level))  # Convert deque to list and add to result
            left_to_right = not left_to_right  # Toggle the direction for the next level

        return result  # Return the final zigzag level order traversal

        