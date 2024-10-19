# Approach - Traverse the array, count consecutive repeating characters, 
# and write the character to the result.
# If the count is greater than 1, 
# write the digits of the count after the character, then continue to the next group.

# TC - O(N)
# SC - O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize the index where we will overwrite in the chars array
        write = 0
        # Start reading from the first character
        read = 0

        # Loop through the chars array
        while read < len(chars):
            # Get the current character
            current_char = chars[read]
            # Initialize a counter to track how many times the current character repeats
            count = 0
            
            # Count the number of consecutive repeating characters
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the character to the array at the 'write' position
            chars[write] = current_char
            write += 1
            
            # If the count is more than 1, write the count to the chars array
            if count > 1:
                # Convert the count to string and write each digit separately
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # Return the length of the new compressed array
        return write
        