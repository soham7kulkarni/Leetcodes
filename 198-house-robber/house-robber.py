# SC - O(N)
# TC - O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)  # Get the number of houses
        if not nums:  # If there are no houses, return 0
            return 0
        if n == 1:  # If there is only one house, return its value
            return nums[0]
        
        arr = [0] * n  # Create an array to store maximum amounts at each house
        arr[0] = nums[0]  # The maximum amount from the first house is its own value
        arr[1] = max(nums[0], nums[1])  # The maximum amount from the first two houses

        # Iterate through the remaining houses starting from the third one
        for i in range(2, n):
            # Decide whether to rob the current house (nums[i]) + amount from two houses back (arr[i-2])
            # or to skip the current house and take the amount from the previous house (arr[i-1])
            arr[i] = max(arr[i-1], nums[i] + arr[i-2])
        
        return arr[-1]  # Return the maximum amount that can be robbed, which is stored in the last element of arr
