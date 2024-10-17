# TC - O(logn)
# SC - O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the binary search
        low = 0
        high = len(nums) - 1

        # Check if the target is at the start or end of the array
        if nums[low] == target:
            return low  # Return the index if found at the start
        if nums[high] == target:
            return high  # Return the index if found at the end

        # Start the binary search loop
        while low <= high:
            # Calculate the mid index
            mid = low + (high - low) // 2
            
            # Check if the mid element is the target
            if nums[mid] == target:
                return mid  # Return the mid index if found

            # Check if the left half of the array is sorted
            elif nums[low] <= nums[mid]:
                # If target is in the left sorted portion
                if nums[mid] > target and target >= nums[low]:
                    # If target is within the range of the left half
                    if target == nums[low]: 
                        return low  # Return low index if target equals nums[low]
                    else:
                        high = mid - 1  # Search in the left half
                else:
                    low = mid + 1  # Search in the right half
            # The right half must be sorted
            else:
                # If target is within the range of the right sorted portion
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1  # Search in the right half
                else:
                    high = mid - 1  # Search in the left half

        # Target not found; return -1
        return -1
