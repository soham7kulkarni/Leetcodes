# TC - O(N)
# SC - O(N)

class Solution:
    def numDecodings(self, s: str) -> int:
        # Length of the input string
        n = len(s)

        # Base case: An empty string can be decoded in one way
        if n == 0 or s[0] == '0':
            return 0

        # dp[i] will hold the number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode a string of length 1 (if it's not '0')

        for i in range(2, n + 1):
            # Check for single digit decode (s[i-1])
            if s[i - 1] != '0':  # Only valid if it's between '1' to '9'
                dp[i] += dp[i - 1]

            # Check for two digits decode (s[i-2:i])
            two_digit = int(s[i - 2:i])  # Get the last two characters
            if 10 <= two_digit <= 26:  # Valid range for '10' to '26'
                dp[i] += dp[i - 2]

        return dp[n]

