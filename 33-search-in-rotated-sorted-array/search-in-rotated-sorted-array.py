class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if target == nums[low]:
            return low
        if target == nums[high]:
            return high
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif nums[low] <= nums[mid]:
                if target < nums[mid] and target >= nums[low]:
                    if nums[low] == target:
                        return low
                    else:
                        high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        