class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i = 0
        j = 0
        count = 0
        queue = deque()
        dirs = [[0,1], [0,-1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, m, n, grid, dirs)
        return count
    def bfs(self, i, j, m, n, grid, dirs) -> None:
        if i < 0 or i ==m or j < 0 or j == n or grid[i][j] == '0': return
        grid[i][j] = '0'
        for direction in dirs:
            nr = i + direction[0]
            nc = j + direction[1]
            self.bfs(nr, nc, m, n, grid, dirs)

        