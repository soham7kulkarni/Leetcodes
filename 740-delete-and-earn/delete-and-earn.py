# TC - O(N) + O(max(N))
# SC - O(max(N))

# it completely depends on maximum value present in nums
# In nums = [1,2,3,10]
# We would be required to create array which will hold 
# sum of i in particular index i. (index 1 will hold sum of 1's)
# (index 10 will hold sum of all 10's)
# In this way we have to create array for 10 elements

# We go thru this array to calculate final max sum. In this case, we have
# to go thru all 10 elements hence tc also depends on max(n)

# It is not applicable when max(n) is small than n
# nums = [1,1,2,2,2,3,3,3,4]
# n > max(n)   :    9 > 4


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Handle edge case: if nums is empty, return 0
        if not nums:
            return 0
        
        # Handle edge case: if there's only one element, return its value
        if len(nums) == 1:
            return nums[0]
        
        # Find the maximum number in nums to define the size of the arr
        maximum = max(nums)

        # Create an array to store the total points for each value
        arr = [0] * (maximum + 1)
        
        # Fill the arr where each index i holds the sum of all occurrences of i in nums
        for i in nums:
            arr[i] += i
        
        # Initialize two variables to track the maximum points at previous two indices
        prev = arr[0]  # Points earned if we take value 0
        curr = max(arr[0], arr[1])  # Max points by either taking 0 or 1
        
        # Iterate through the arr starting from index 2 to calculate max points
        for i in range(2, len(arr)):
            # Store the current value of curr before updating it
            temp = curr
            
            # Update curr to be the maximum of not taking or taking the current value
            curr = max(curr, arr[i] + prev)
            
            # Move prev to the last known curr value
            prev = temp
            
        # Return the maximum points that can be earned
        return curr
        