# TC - O(M+N)
# SC - O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for 's' (the subsequence string)
        i = 0  
        # Pointer for 't' (the longer string)
        j = 0  

        # Traverse through the longer string 't'
        while i < len(s) and j < len(t):
            # If characters match, move to the next character in 's'
            if s[i] == t[j]:
                i += 1
            # Always move to the next character in 't'
            j += 1

        # If the pointer i has traversed all characters in 's', return True
        return i == len(s)