class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            res[i] = self.solve(i, res)
        return res
    def solve(self, i, res):
        if i == 0: return 0
        if i == 1: return 1

        if res[i] != 0: return res[i]
        if i%2 == 0:
            res[i] = self.solve(i//2, res)
            return res[i]
        else:
            res[i] = 1 + self.solve(i//2, res)
            return res[i]
        