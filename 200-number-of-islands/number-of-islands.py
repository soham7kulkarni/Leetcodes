# Approach - BFS
# TC - O(M*N)
# EXACT - 2(MN) In worst case (all 1s), We convert every 1 to 0 in first pass 
# for loop. But still we check all 0s to complete the for loop 
# hence we touch every element at least twice.
# SC - O(M*N)
# EXACT - min(m,n) Consider skew matrix and then check the length of the longest diagonal
# Not necessarily length of diagonal but the number of elements

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        queue = deque()
        dirs = [[0,1], [0,-1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    queue.append((i, j))
                    while queue:
                        curr = queue.popleft()
                        for direction in dirs:
                            nr = curr[0] + direction[0]
                            nc = curr[1] + direction[1]
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))
        return count


        