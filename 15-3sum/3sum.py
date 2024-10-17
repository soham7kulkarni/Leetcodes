# TC - N^2+nlogn i.e n^2
# SC - O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to facilitate the two-pointer approach
        nums.sort()
        n = len(nums)  # Get the length of the sorted array
        arr = []  # Initialize a list to store the result triplets

        # Iterate through the array, stopping 2 elements before the end
        for i in range(n - 2):
            # If the current number is greater than 0, we can break the loop
            # since the array is sorted and there won't be any valid triplets
            if nums[i] > 0:
                break
            
            # Initialize two pointers: one just after the current element (low)
            # and the other at the end of the array (high)
            low = i + 1
            high = n - 1
            
            # Skip duplicate elements for the current index to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find pairs that sum to the negative of nums[i]
            while low < high:
                # Calculate the sum of the current triplet
                sum = nums[i] + nums[low] + nums[high]

                # If the sum is zero, we found a triplet
                if sum == 0:
                    res = [nums[i], nums[low], nums[high]]
                    arr.append(res)  # Add the triplet to the result list

                    # Move both pointers inward
                    low += 1
                    high -= 1
                    
                    # Skip duplicate values for the 'low' pointer
                    while low < n - 1 and nums[low] == nums[low - 1]:
                        low += 1
                    
                    # Skip duplicate values for the 'high' pointer
                    while high >= 0 and nums[high] == nums[high + 1]:
                        high -= 1
                
                # If the sum is greater than zero, move the 'high' pointer left
                elif sum > 0:
                    high -= 1
                
                # If the sum is less than zero, move the 'low' pointer right
                else:
                    low += 1
        
        return arr  # Return the list of unique triplets
