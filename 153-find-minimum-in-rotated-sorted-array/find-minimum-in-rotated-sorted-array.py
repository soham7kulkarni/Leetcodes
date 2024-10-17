#Approach 1 - linearly compare adjacent elements adn return min value : TC - O(n)
#Approach 2 - Minium element wil have greater elemnts on both sides. 
# First check if array is rotated or not by comparing values of low and high.
# If array is not rotated it means low has pivot. 
# If it is rotated, calculate mid. Handle edge cases for both sides. 
# If middle is on left, cant comapre with another left element. 
# If its on right side we already got it covered by stating if low <= high at start of while loop
# Choose the side which is not sorted. TC - O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while (low <= high):
            # When we go inside distorted half
            # Before calculating mid, we check once
            if nums[low] <= nums[high]: return nums[low]
            mid = low + (high-low)//2
            if (nums[mid] == 0 or nums[mid] < nums[mid-1]) and nums[mid] < nums[mid+1]: return nums[mid]
            elif nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            
        