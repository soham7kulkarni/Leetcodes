# - We go though each letter in s - O(N)
# - For every letter we go though word dict 
# checking if any available word is matching - O(M)
# - To match word with possible window, in worst case it could be O(N)
# -  Case where we have leetcode word in word dict, 
# we match every character after coming to first element

# TC - O(N*M*N)
# SC - O(N)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a DP array with size len(s) + 1, initialized to False
        # dp[i] will be True if the substring s[0:i] can be segmented into words from the dictionary
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: an empty string can always be segmented
        
        # Iterate through the string in reverse
        for i in range(len(s) - 1, -1, -1):
            # Check each word in the dictionary
            for w in wordDict:
                # Check if the current word can fit into the substring s[i:]
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    # If it matches, set dp[i] based on the DP value of the remaining substring
                    dp[i] = dp[i + len(w)]
                # If dp[i] is True, no need to check further words
                if dp[i]:
                    break
        
        return dp[0]  # Return whether the entire string can be segmented

