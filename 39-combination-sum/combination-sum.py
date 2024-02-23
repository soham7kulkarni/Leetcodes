# Approach - choose or not choose
# Cons - exponential time and space complexity. We create deep copy of path everytime we choose node
# TC - 2^(M*N)
# SC - 2^(M*N)

class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return self.result
        self.helper(candidates, 0, target, [])
        return self.result

    def helper(self, candidates, index, target, path):
        # base
        if target == 0:
            self.result.append(path) # If we return path then it will have all the elements
            # from the path we traversed.
            # Hence creating deep copy of the path and return is necessary 
            return
        if index == len(candidates) or target < 0: return
        # logic
        # don't choose
        self.helper(candidates, index+1, target, path)
        # choose
        li = path[:]
        li.append(candidates[index])
        self.helper(candidates, index, target-candidates[index], li)
        