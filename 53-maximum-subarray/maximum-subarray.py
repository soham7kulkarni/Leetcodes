# If at any point the sum becomes negative
# we will set the sum to 0 as we are not going to consider it as a part of our answer.

# TC - O(N)
# SC - O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if total > maximum:
                maximum = total
            if total < 0:
                total = 0
        return maximum
        