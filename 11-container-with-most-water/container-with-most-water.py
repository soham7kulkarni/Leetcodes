# TC - O(N)
# SC - O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0  # Initialize the left pointer
        j = len(height) - 1  # Initialize the right pointer
        maxArea = 0  # Variable to keep track of the maximum area

        # Continue until the two pointers meet
        while i < j:
            length = j - i  # Calculate the width of the container
            currentHeight = min(height[i], height[j])  # Find the height of the container
            area = length * currentHeight  # Calculate the area of the container
            
            # Update the maximum area found so far
            maxArea = max(maxArea, area)

            # Move the pointer pointing to the shorter line
            if height[i] < height[j]:
                i += 1  # Move the left pointer to the right
            else:
                j -= 1  # Move the right pointer to the left

        return maxArea  # Return the maximum area found
