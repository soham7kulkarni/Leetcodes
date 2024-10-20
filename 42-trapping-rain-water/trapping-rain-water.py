# Approach 1 - traversing throuh array from left till end 
# and finding maximum left height for every index. 
# Repeating same from right till start for maximum right height. 
# The max capacity of water stored at particular index is 
# min(leftmax and right max) - value of index. 
# Calculating for all index positions and getting sum of them.

# TC - O(N)  SC - O(N)

# Approach 2 - Taking two pointers at two ends. 
# Storing capacity bottleneck occurs due to min height 
# and hence just start with leftmax and rightmax. 
# Take minimum of them and do subtraction for particular index. 
# Update leftmax or rightmax and then decide to continue with the one with least value. 
# Traverse from both sides till they cross each other. 
# Also we cannot store water at both ends.

# TC - O(N)
# SC - O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # Check if the input list is empty; if so, return 0 as no water can be trapped
        if not height:
            return 0

        # Get the length of the height array
        n = len(height)

        # Initialize left pointer at the start (0) and right pointer at the end (n-1)
        l = 0
        r = n - 1

        # Initialize a variable to accumulate the total trapped water
        arr = 0

        # Initialize leftMax and rightMax to the first and last heights respectively
        leftmax, rightmax = height[l], height[r]

        # Loop until the left pointer is less than the right pointer
        while l < r:
            # Compare the maximum heights from the left and right
            if leftmax < rightmax:
                # Move the left pointer to the right
                l += 1
                
                # Update leftMax to the maximum of current leftMax and the new height at the left pointer
                leftmax = max(leftmax, height[l])

                # Calculate the water trapped at the current left index
                arr += leftmax - height[l]  # Add the trapped water at the left position
            else:
                # Move the right pointer to the left
                r -= 1
                
                # Update rightMax to the maximum of current rightMax and the new height at the right pointer
                rightmax = max(rightmax, height[r])

                # Calculate the water trapped at the current right index
                arr += rightmax - height[r]  # Add the trapped water at the right position

        # Return the total amount of trapped water
        return arr