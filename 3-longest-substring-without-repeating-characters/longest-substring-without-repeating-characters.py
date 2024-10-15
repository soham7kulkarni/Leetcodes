# We can put the characters in set and can check the length of longest substring
# Hence we use counter to count number of appearance of the letters. 
# { "a": 1, "b": 1} and update length of result
# We run two pointers and left will catch up with right if we receive duplicate letter. 
# As the value of the letter becomes more than 1 in the counter
# TC - O(N)
# SC - O(1)
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0  # Left pointer for the sliding window
        right = 0  # Right pointer for the sliding window
        maxLength = 0  # Maximum length of substring found
        counter = Counter()  # Counter to track character frequencies
        
        # Expand the right pointer to include new characters
        while right < len(s):
            ch = s[right]  # Current character to consider
            counter[ch] += 1  # Increment the count of the character
            
            # If there is a duplicate character, move the left pointer
            while counter[ch] > 1:
                c = s[left]  # Character at the left pointer
                counter[c] -= 1  # Decrease its count
                left += 1  # Move the left pointer to the right
            
            # Update the maximum length if the current window is larger
            maxLength = max(maxLength, right - left + 1)
            right += 1  # Move the right pointer to the right
        
        return maxLength  # Return the length of the longest substring

        