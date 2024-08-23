class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        t = len(nums) - 1
        i = 0
        while i <= t:
            if nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[z], nums[i] = nums[i], nums[z]
                i += 1
                z += 1       