class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return self.result
        self.helper(candidates, target, 0, [])
        return self.result

    def helper(self, candidates, target, pivot, path):
        if target < 0 or pivot == len(candidates): return 
        if target == 0:
            self.result.append(path)
            return

        for i in range(pivot, len(candidates)):
            li = path[:]
            li.append(candidates[i])
            self.helper(candidates, target-candidates[i], i, li)

