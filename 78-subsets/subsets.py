# Approach - For loop based recursion
# Every step, we record the generated path in result then we add current element to path
# Then we recurse but this time starting point is current element
# TC - O(2^n)

class Solution:
    # Constructor to initialize an instance variable to store results
    def __init__(self):
        # Initialize an empty list to store all the subsets
        self.result = []
    
    # Main function to return all subsets of the given list of numbers
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start the recursive helper function to generate subsets
        self.helper(nums, 0, [])
        # Return the list of all subsets after helper completes
        return self.result
    
    # Helper function for recursive subset generation
    def helper(self, nums, idx, path):
        # Add the current subset (path) to the result list
        # This line ensures every possible subset (partial or complete) is recorded
        self.result.append(path[:])  # Append a copy of path to avoid mutation
        
        # Iterate from the current index to the end of the list
        for i in range(idx, len(nums)):
            # Choice: include nums[i] in the subset
            path.append(nums[i])
            # Recur with the next index after i, to build further subsets
            self.helper(nums, i + 1, path)
            # Backtrack: remove the last element to explore other combinations
            path.pop()
