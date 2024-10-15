class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # Left pointer for the sliding window
        maxLength = 0  # Maximum length of the substring found
        count = defaultdict(int)  # Dictionary to count occurrences of each character
        maxCount = 0  # The count of the most frequently occurring character in the current window

        for right in range(len(s)):
            count[s[right]] += 1  # Increment the count for the current character
            maxCount = max(maxCount, count[s[right]])  # Update the count of the most common character

            # If the current window size minus the most frequent character's count is greater than k,
            # it means we need to shrink the window
            if (right - left + 1) - maxCount > k:
                count[s[left]] -= 1  # Decrease the count of the leftmost character
                left += 1  # Move the left pointer to the right

            # Update the maximum length of the valid substring found so far
            maxLength = max(maxLength, right - left + 1)

        return maxLength  # Return the length of the longest valid substring