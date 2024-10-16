# Approach - For any step i, the number of distinct ways to reach that step 
# can be derived from the sum of ways to reach the previous step 
# and the step before that
# you can either come from step i-1 
# (taking a single step) or from step i-2 (taking two steps)

# TC - O(N)
# SC - O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        
        
        # Base cases
        first = 1  # 1 way to stay at the ground (do nothing)
        second = 1  # 1 way to climb to the first step
        
        # Fill the dp array using the recurrence relation
        for i in range(2, n + 1):
            current = first + second
            second = first
            first = current
        
        return current  # Return the number of ways
        