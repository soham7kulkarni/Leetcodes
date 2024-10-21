# TC - O(N)
# SC - O(1)

# Approach - Instead of calculating all subsets of ke length and tracking max average (n*k)
# We use sliding window, we update sum by sutrackting left element and adding right element
# Max average is returned

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first subarray of length k
        current_sum = sum(nums[:k])
        max_sum = current_sum  # Initialize max_sum to the sum of the first subarray
        
        # Slide the window over the array from the k-th element to the end
        for i in range(k, len(nums)):
            # Update the current sum by subtracting the element that goes out of the window
            # and adding the new element that comes into the window
            current_sum = current_sum - nums[i - k] + nums[i]
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / k
        