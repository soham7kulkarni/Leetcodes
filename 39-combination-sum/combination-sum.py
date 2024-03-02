class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return self.result
        self.helper(candidates, target, 0, [])
        return self.result

    def helper(self, candidates, target, pivot, path):
        # base
        if target == 0: 
            self.result.append(path[:])
            return
        if target < 0 or pivot == len(candidates): return 

        # don't choose
        self.helper(candidates, target, pivot + 1, path)
        # action
        path.append(candidates[pivot])
        # choose
        self.helper(candidates, target - candidates[pivot], pivot, path)
        # pop
        path.pop()
