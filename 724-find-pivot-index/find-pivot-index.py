# Approach 1 - Calculate left sum and right sum for each index
# then check both values for each index

# Approach 2 - Calculate total sum (left half + right half)
# For each index, just subtract left sum from total as well as that number (this is right half)
# check if left half is equal to right half

# TC - O(N)
# SC - O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate total sum of the array
        left_sum = 0  # Initialize left sum to 0

        for i in range(len(nums)):
            # Check if left sum equals right sum
            if left_sum == total_sum - left_sum - nums[i]:
                return i  # Return the pivot index

            left_sum += nums[i]  # Update left sum by adding the current element

        return -1  # Return -1 if no pivot index is found
        