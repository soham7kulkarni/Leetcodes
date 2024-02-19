# Approach - DFS
# From first rotten orange, we start DFS, we visit all the other nodes and record
# time it will take to turn them rotten.
# Then we check if we can reach particular node, if we have any better path (minimum time) from any other rotten orange(node).
# If Yes, we update its value and then again all its neighbors values if possible
# 3 < 6, keep it as it is (since we wont override 7 with 3)
# 9 < 9, yes, override 9 with 7
# TC - O(MN * MN)
# SC - O(MN)
class Solution:
    def __init__(self):
        self.dirs = [[0,-1], [-1,0], [0,1], [1,0]]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m = len(grid) #number of rows
        n = len(grid[0]) #number of columns
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.dfs(grid, i, j, 2, m, n)
        maximum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1 # Still fresh
                maximum = max(maximum, grid[i][j] - 2)
        return maximum
       
    def dfs(self, grid, r, c, time, m, n):
        #base
        if (r < 0 or c < 0 or r == m or c == n): return
        if grid[r][c] != 1 and grid[r][c] < time: return # We never go to 0 and optimized nodes. We visit only those nodes which are either 1 (fresh) or the ones we can optimize
        
        #logic
        grid[r][c] = time
        for d in self.dirs:
            nr = r + d[0]
            nc = c + d[1]
            self.dfs(grid, nr, nc, grid[r][c]+ 1, m, n)

        