# Approach - Sliding window
# checking if incoming element is duplicate by using set, 
# if yes - shrink the window from left and continue till we get rid of duplicate
# if no - add right node to set and calculate sum of window
# only comapre with resultant sum when window length is k
# In the next iteration, we will add non duplicate incoming right element to cur sum
# Hence in current iteration, we remove left from window

# Suppose window is 3, next time it becomes 4. to avoid, we reduce it early to 2


# TC - O(N) 
# SC - O(K), length of set




class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0  # Initialize max_sum to 0
        current_sum = 0  # Initialize current sum to 0
        left = 0  # Initialize the left pointer of the sliding window
        seen = set()  # Create a set to store distinct elements in the current window
        
        # Iterate through the array using the right pointer of the sliding window
        for right in range(len(nums)):
            while nums[right] in seen:  # If the element is already seen, shrink the window
                seen.remove(nums[left])  # Remove the leftmost element
                current_sum -= nums[left]  # Adjust the current sum
                left += 1  # Move the left pointer to the right
            
            # Add the current element to the window
            seen.add(nums[right])  # Add the current element to the set
            current_sum += nums[right]  # Update the current sum
            
            # If we have a valid window of size k, update max_sum
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)  # Update max_sum if necessary

                # Remove the leftmost element from the window for the next iteration
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1  # Move the left pointer to the right
        
        return max_sum  # Return the maximum sum found
        