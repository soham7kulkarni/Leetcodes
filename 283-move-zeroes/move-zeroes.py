# Approach - Traverse the array, and for each non-zero element, 
# shift it to the front of the array while keeping track of the next available position for non-zero values.
# After all non-zero elements are moved, fill the remaining positions with zeroes.

# TC - O(N)
# SC - O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer to keep track of the position to place non-zero elements
        left = 0
        
        # Traverse through the array
        for num in nums:
            # If the current number is non-zero, place it at the non_zero_index position
            if num != 0:
                nums[left] = num
                left += 1
        
        # After all non-zero elements are moved, fill the remaining positions with zeros
        for i in range(left, len(nums)):
            nums[i] = 0
        