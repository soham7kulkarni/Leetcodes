# TC - O(N)
# SC - O(1)

# Approach - check the window. 
# If in present window, we have k 0's 
# then we will count the size of window (part of valid answer)
# When we have k 0's, next time we not only increase window 
# but also decrease the window by left +=1


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_len = 0  # Variable to store the maximum length of the subarray
        zeros_count = 0  # Count of zeros in the current window
        
        # Iterate over the array using the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:  # If the current element is a zero, increment zeros_count
                zeros_count += 1
            
            # If the number of zeros exceeds k, shrink the window by moving the left pointer
            while zeros_count > k:
                if nums[left] == 0:  # Decrement zeros_count if the left element is zero
                    zeros_count -= 1
                left += 1  # Move the left pointer to shrink the window
            
            # Update the max_len with the current window size
            max_len = max(max_len, right - left + 1)
        
        return max_len
            