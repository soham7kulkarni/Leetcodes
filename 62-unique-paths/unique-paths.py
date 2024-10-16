# TC - O(MN)
# SC - O(MN)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D list to store the number of unique paths to each cell
        dp = [[0] * n for _ in range(m)]
        
        # Fill the first row with 1s (only one way to reach each cell in the first row)
        for j in range(n):
            dp[0][j] = 1
            
        # Fill the first column with 1s (only one way to reach each cell in the first column)
        for i in range(m):
            dp[i][0] = 1
            
        # Fill the rest of the dp table using the recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The bottom-right cell contains the number of unique paths to reach it
        return dp[m-1][n-1]

        