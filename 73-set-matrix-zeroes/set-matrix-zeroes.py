# Approach 1 - Creating two arrays of size m and n
# whenever matrix[i][j] == 0, we mark respective i and j in thpse arrays as 1
# Helps in keeping track of which rows and cols to make 0 later

# TC - O(MN)
# SC - O(N + M)

# Approach 2 - Using first row and first col. Wheneve we find 0 we mark
# first element of that row as 0 and first element of that column as 0
# When we traverse again thru matrix we mark the entire row and col with 0 as 0
# if 0 is found in 0th row we mark matrix[0][0] as 0. It doesn't mean 0th column is 0
# To clear this, we maintain variable col0 and if it is 0 then only we turn 0th column in 0

# TC - O(2MN)
# SC - O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        m = len(matrix)
        n = len(matrix[0])
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # mark i-th row:
                    matrix[i][0] = 0

                    # mark j-th column:
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        #step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix
        