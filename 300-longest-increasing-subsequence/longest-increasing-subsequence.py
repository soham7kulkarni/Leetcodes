# TC - O(n^2)
# sc - O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:  # Check if the input list is empty
            return 0

        n = len(nums)  # Length of the input list
        dp = [1] * n  # Initialize dp array with 1s

        # Iterate through the nums array
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:  # Check if we can extend the increasing subsequence
                    dp[i] = max(dp[i], dp[j] + 1)  # Update the dp[i] value

        return max(dp)  # The longest increasing subsequence length is the maximum in dp
