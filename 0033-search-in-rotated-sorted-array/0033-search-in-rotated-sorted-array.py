# First compare middle element and return if it matches the target. After you divide array in two parts one side will always be sorted. Start with that side and check if element lies in range or else discard that side and move to other side. repeat it till the end.
# Time Complexity - O(logn)

# Another solution is sorting array/unrotating array. logn for sorting the array and then logn to find the target. logn+logn

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            else: 
                if nums[mid] < target and nums[high] >=target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1 

                