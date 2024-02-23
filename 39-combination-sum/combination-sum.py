# Approach - for loop backtrack

class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return self.result
        self.helper(candidates, 0, target, [])
        return self.result

    def helper(self, candidates, pivot, target, path):
        # base
        if target == 0:
            self.result.append(path[:]) # If we return path then it will have all the elements
            # from the path we traversed.
            # Hence creating deep copy of the path and return is necessary 
            return
        if pivot == len(candidates) or target < 0: return

        # logic

        for i in range(pivot, len(candidates)):
           path.append(candidates[i])
           self.helper(candidates, i ,target - candidates[i],path)
           #                      pivot moves from i onwards
           path.pop()

        