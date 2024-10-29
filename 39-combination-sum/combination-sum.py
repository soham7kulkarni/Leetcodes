# Approach - 
# 1. Backtrack after you counting element inside path
# 2. Add path to resultant list only after meeting sum combination
# 3. Everytime create deep copy of path and add it to result
# 4. Else same path variable will be addressed everytime and if we have performed backtracking
# we return null as a path

# TC - O(2**MN)

class Solution:
    # Constructor to initialize an empty result list
    def __init__(self):
        self.result = []

    # Main function to find all unique combinations that sum up to the target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # If the candidate list is empty, return the current result (which is also empty)
        if not candidates: 
            return self.result
        # Start the helper function with initial parameters
        self.helper(candidates, target, 0, [])
        return self.result

    # Helper function to explore all possible combinations recursively
    def helper(self, candidates, target, pivot, path):
        # Base case 1: If the target becomes 0, we found a valid combination
        if target == 0:
            # Add a copy of the current path to the result list
            self.result.append(path[:])
            return
        # Base case 2: If target is negative or we've checked all candidates, stop recursion
        if target < 0 or pivot == len(candidates): 
            return

        # Recursive case 1: Skip the current candidate (don't choose it)
        self.helper(candidates, target, pivot + 1, path)

        # Action: Choose the current candidate by adding it to the path
        path.append(candidates[pivot])

        # Recursive case 2: Include the current candidate in the sum and keep it in the path
        # Call helper with updated target and the same candidate (for repeated usage)
        self.helper(candidates, target - candidates[pivot], pivot, path)

        # Backtracking step: Remove the last element to explore other possibilities
        path.pop()
