# Approach -
# Check length of two words
# Check set of characters present (only 1 char is allowed)
# Check frequency of characters 

# TC - O(N)
# SC - O(26) - O(1)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: If the lengths are not equal, return false
        if len(word1) != len(word2):
            return False
        
        # Step 2: Check if both words have the same unique characters
        if set(word1) != set(word2):
            return False
        
        # Step 3: Count the frequency of each character in both strings
        freq1 = Counter(word1)  # Frequency of characters in word1
        freq2 = Counter(word2)  # Frequency of characters in word2
        
        # Step 4: Count how many characters have each frequency
        freq_count1 = Counter(freq1.values())  # Count frequencies in word1
        freq_count2 = Counter(freq2.values())  # Count frequencies in word2
        
        # Step 5: Compare the frequency counts
        return freq_count1 == freq_count2
        