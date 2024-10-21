# Approach - Perform BFS
# Calculate sum at each level and update maxLevel as well as maxSum

# TC - O(N)
# SC - O(W)is the maximum width of the tree. 
# In the worst case, the queue can store all nodes at a single level. 
# For a perfectly balanced tree, this is \U0001d442(\U0001d45b/2)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:  # Check if the tree is empty
            return 0

        max_sum = float('-inf')  # Initialize maximum sum to negative infinity
        max_level = 0  # Initialize level with the maximum sum
        current_level = 1  # Start with the first level

        # Initialize a queue for level order traversal
        queue = deque([root])  

        while queue:
            level_sum = 0  # Initialize sum for the current level
            level_size = len(queue)  # Get the number of nodes at the current level

            for _ in range(level_size):  # Traverse all nodes at the current level
                node = queue.popleft()  # Get the front node in the queue
                level_sum += node.val  # Add its value to the level sum
                
                # Add child nodes to the queue for the next level
                if node.left:  
                    queue.append(node.left)
                if node.right:  
                    queue.append(node.right)

            # Check if the current level's sum is greater than the maximum sum recorded
            if level_sum > max_sum:
                max_sum = level_sum  # Update maximum sum
                max_level = current_level  # Update the level of maximum sum

            current_level += 1  # Move to the next level

        return max_level  # Return the level with the maximum sum

        