# Approach - Generate all substrings and check if it has unique characters

# Approach 2 - Start traversing thru charcaters. 
# Add charcaters to set
# Whenever we found duplicate charcater, we increment partition count by 1 and clear the set

# TC - O(N)
# SC - O(26) - Set will have 26 characters in worst case

class Solution:
    def partitionString(self, s: str) -> int:
        # Initialize a set to track unique characters in the current substring
        unique_chars = set()
        # Initialize partition count, starting with 1
        partitions = 1
        
        # Iterate over each character in the string
        for char in s:
            # If character is already in the set, start a new partition
            if char in unique_chars:
                partitions += 1  # Increment partition count
                unique_chars.clear()  # Clear the set to start a new substring
            
            # Add the current character to the set of unique characters
            unique_chars.add(char)
        
        # Return the total number of partitions needed
        return partitions
