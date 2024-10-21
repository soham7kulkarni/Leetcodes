# TC - O(N)
# SC - O(1)

# Approach - we check the number of zeros in current window
# If it exceeds k value, then we not only increase window from right
# but also decrease window from left, to keep only k zeros
# We traverse our left till we keep zeros below k

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer of the sliding window
        zero_count = 0  # Number of zeros in the current window
        max_len = 0  # Store the maximum length of valid subarray

        for right in range(len(nums)):
            if nums[right] == 0:  # Count zeros
                zero_count += 1

            # If more than one zero, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Move the left pointer to shrink the window

            # Calculate the current valid window size, subtracting one to account for the "deletion"
            max_len = max(max_len, right - left)

        return max_len if max_len != len(nums) else max_len - 1  # Handle edge case where array is all 1s
            