# TC - O(N^2)
# SC - O(1)

# The algorithm examines each character in the string (n) and, for each character, expands 
# around it in both directions, potentially visiting all characters in the string (n). 
# Thus, the overall time complexity is O(n^2).

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the input string has length 0 or 1, return it as it is already a palindrome.
        if len(s) <= 1:
            return s

        # Helper function to expand around a given center and return the longest palindrome found.
        def expand_from_center(left, right):
            # Continue expanding as long as the characters at left and right are the same
            # and the indices are within bounds.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Move left pointer outward
                right += 1  # Move right pointer outward
            # Return the found palindrome. Adjust indices to exclude the last unmatched characters.
            return s[left + 1:right]

        max_str = s[0]  # Initialize the longest palindromic substring with the first character.

        # Iterate over each character in the string to consider it as a center.
        for i in range(len(s) - 1):
            # Check for odd-length palindromes (single character center).
            odd = expand_from_center(i, i)
            # Check for even-length palindromes (two character center).
            even = expand_from_center(i, i + 1)

            # Update max_str if the found odd-length palindrome is longer than the current max.
            if len(odd) > len(max_str):
                max_str = odd
            # Update max_str if the found even-length palindrome is longer than the current max.
            if len(even) > len(max_str):
                max_str = even

        # Return the longest palindromic substring found.
        return max_str

