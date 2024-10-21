# TC - O(N)
# SC - O(1)

# Approach - count number of vowels in first window
# Update window and update the count of vowels
# Return the max_vowel count

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')  # Define a set of vowels for quick lookup
    
        # Count the number of vowels in the first window of size k
        current_vowel_count = sum(1 for char in s[:k] if char in vowels)
        max_vowels = current_vowel_count  # Initialize max_vowels with the first window's count
        
        # Slide the window from position k to the end of the string
        for i in range(k, len(s)):
            # Subtract the influence of the character that is leaving the window
            if s[i - k] in vowels:
                current_vowel_count -= 1
            # Add the influence of the character that is entering the window
            if s[i] in vowels:
                current_vowel_count += 1
            
            # Update max_vowels if necessary
            max_vowels = max(max_vowels, current_vowel_count)
        
        return max_vowels
        