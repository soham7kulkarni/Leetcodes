# Approach - By comparing the cells from above and to the left, 
# we effectively consider both possibilities of excluding one character at a time 
# and gradually build towards the longest common subsequence through the table.

# TC - O(MN)
# SC - O(MN)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)  # Length of the first string
        n = len(text2)  # Length of the second string

        # Create a 2D array (dp) with (m+1) x (n+1) to store the lengths of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(1, m + 1):  # Loop through each character in text1
            for j in range(1, n + 1):  # Loop through each character in text2
                # If characters match, increment the length of the LCS
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise, take the maximum from the left or top cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The length of the longest common subsequence will be in the bottom-right cell
        return dp[m][n]