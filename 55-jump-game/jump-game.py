# TC - O(N)
# SC - O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The farthest index we can reach
        farthest = 0
        n = len(nums)

        for i in range(n):
            # If the current index is beyond the farthest we can reach, return False
            if i > farthest:
                return False
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            # If we can reach the last index, return True
            if farthest >= n - 1:
                return True
        
        # If we exit the loop, it means we can't reach the last index
        return False
