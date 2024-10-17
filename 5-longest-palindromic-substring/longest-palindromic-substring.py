# TC - O(N^2)
# SC - O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""  # Return empty string if input is empty
        
        start, end = 0, 0  # Pointers to store the starting and ending indices of the longest palindrome found
        
        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            len1 = self.expandAroundCenter(s, i, i)
            # Check for even-length palindromes (two character center)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)  # Get the maximum length of the palindromes found
            
            # Update start and end indices if we found a longer palindrome
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]  # Return the longest palindromic substring
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1  # Expand left
            right += 1  # Expand right
        return right - left - 1  # Return the length of the palindrome found
