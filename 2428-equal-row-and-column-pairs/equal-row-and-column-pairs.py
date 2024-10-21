# Brute Force - Traversing thru each row and column and check equality

# Optimal Approach - Storing the elements as a tuple in dictionary
# Value is frequency of that row
# Checking if column of values is already present in dictionary
# (it will mean row and column is equal)

# TC - O(N*N) N*N are total elements present
# SC - O(N)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Step 1: Count occurrences of each row
        row_count = Counter(tuple(row) for row in grid)
        
        # Step 2: Initialize a count for equal pairs
        count = 0
        
        # Step 3: Iterate through each column in the grid
        for c in range(len(grid)):
            # Construct the column as a tuple
            col = tuple(grid[r][c] for r in range(len(grid)))
            
            # Step 4: Add the count of this column in the row_count
            count += row_count[col]
            
        return count
        