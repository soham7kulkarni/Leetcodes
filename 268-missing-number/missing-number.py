class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = 0
        size = len(nums)
        for i in range(size+1):
            if i not in nums:
                temp = i
                break
        return temp
        