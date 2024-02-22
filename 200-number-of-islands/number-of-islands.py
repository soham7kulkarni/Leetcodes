# Approach - DFS
# TC - O(M*N)
# SC - O(M*N)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0,-1], [0,1], [-1,0], [1,0]]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, m, n, dirs)
        return count

    def dfs(self, grid, i, j , m, n, dirs):
        # base
        if i < 0 or j < 0 or i == m or j == n or grid[i][j] == "0": return
        # logic
        grid[i][j] = "0"
        for d in dirs:
            r = i + d[0]
            c = j + d[1]
            self.dfs(grid, r, c, m, n, dirs)
       
                    

        