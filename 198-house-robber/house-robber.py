# SC - O(1)
# TC - O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)  # Get the number of houses
        if not nums:  # If there are no houses, return 0
            return 0
        if n == 1:  # If there is only one house, return its value
            return nums[0]
        
        
        prev = nums[0]  # The maximum amount from the first house is its own value
        curr = max(nums[0], nums[1])  # The maximum amount from the first two houses

        # Iterate through the remaining houses starting from the third one
        for i in range(2, n):
            # our current changes and we want our prev to point at last curr
            # hence we store curr in temp and prev goes to temp to keep track of past values
            temp = curr
            # We override curr with max value at that cell
            curr = max(curr, nums[i] + prev)
            # our prev moves to previous curr that is temp
            prev = temp
        
        return curr  # Return the maximum amount that can be robbed, which is stored in the last element of arr
