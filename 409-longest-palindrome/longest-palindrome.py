class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize an empty set to track characters that appear an odd number of times
        set1 = set()
        # Initialize a counter to store the length of the palindrome
        count = 0

        # Iterate over each character in the input string
        for i in s:
            # Check if the character is already in the set
            if i in set1:
                # If it is, that means we have seen this character an even number of times
                # Increment count by 2 (as both characters can be used in the palindrome)
                count += 2
                # Remove the character from the set, as it now has an even frequency
                set1.remove(i)
            else:
                # If it's not in the set, add it, marking this character as seen an odd number of times
                set1.add(i)

        # After looping through all characters, if there are any characters left in the set,
        # we can use one of them as a center character in the palindrome
        if len(set1) != 0:
            count += 1

        # Return the total count, which represents the maximum length of the palindrome
        return count
