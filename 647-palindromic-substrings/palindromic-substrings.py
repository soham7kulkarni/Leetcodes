# TC - O(n2)
# SC - O(1)
class Solution:
    def __init__(self):
        self.count = 0  # Initialize the count of palindromic substrings

    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):  # Iterate over each character in the string
            self.helper(s, i, i)  # Check for odd-length palindromes centered at i
            self.helper(s, i, i + 1)  # Check for even-length palindromes centered between i and i+1
        return self.count  # Return the total count of palindromic substrings

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:  # Expand while the characters match
            self.count += 1  # Increment the count for each palindrome found
            left -= 1  # Move left pointer to expand
            right += 1  # Move right pointer to expand

        
        