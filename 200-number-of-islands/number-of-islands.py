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
        m = len(grid)  # Get the number of rows in the grid
        n = len(grid[0])  # Get the number of columns in the grid
        count = 0  # Initialize the island count to zero
        queue = deque()  # Create a queue to help with BFS
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Define the directions for right, left, down, and up

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # Check if the cell is land ('1')
                if grid[i][j] == '1':
                    count += 1  # Found an island, increment the count
                    queue.append((i, j))  # Add the current cell to the queue

                    # Perform BFS to mark all parts of the island
                    while queue:
                        curr = queue.popleft()  # Get the current cell from the queue
                        # Explore all four possible directions
                        for direction in dirs:
                            nr = curr[0] + direction[0]  # New row index
                            nc = curr[1] + direction[1]  # New column index
                            # Check if the new indices are within bounds and the cell is land ('1')
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'  # Mark the cell as visited (change '1' to '0')
                                queue.append((nr, nc))  # Add the cell to the queue for further exploration

        return count  # Return the total number of islands found
