# We need to consider 2 cases here, 
# either we include first house and exclude last house
# Or we exclude first house (automatically starting from 2)
# When we start from 2, its straight forward
# When we start from 1, we need to handle circular list hence 2 cases
# Rest is straight forward house robber

# TC - O(N)
# SC - O(1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    def helper(self, houses) -> int:
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        
        prev = houses[0]  # The maximum amount from the first house is its own value
        curr = max(houses[0], houses[1])  # The maximum amount from the first two houses

        for i in range(2, len(houses)):
            temp = curr
            # We override curr with max value at that cell
            curr = max(curr, houses[i] + prev)
            # our prev moves to previous curr that is temp
            prev = temp
        return curr