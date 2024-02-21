# Approach - BFS
# TC - O(M*N)
# EXACT - 2(MN) In worst case (all 1s), We convert every 1 to 0 in first element 
# for loop. But still we check all 0s to complete the for loop hence we touch every element at least twice.
# SC - O(M*N)
# EXACT - min(m,n) Consider skew matrix and then check the length of the longest diagonal

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0,-1], [0,1], [-1,0], [1,0]]
        q = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    q.append((i,j))
                    grid[i][j] = "0"
                    count += 1
                    while q:
                        curr = q.popleft()
                        for d in dirs:
                            nr = d[0] + curr[0]
                            nc = d[1] + curr[1]
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                                q.append((nr,nc))
                                grid[nr][nc] = "0"
        return count

        