class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 == str2 + str1, to confirm they have a common divisor pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the smaller string length
        min_len = min(len(str1), len(str2))
        
        # Iterate from the largest possible divisor (min_len) down to 1
        for i in range(min_len, 0, -1):
            # Check if the current length can divide both strings
            if len(str1) % i == 0 and len(str2) % i == 0:
                # The candidate divisor is the first i characters of str1
                candidate = str1[:i]
                
                # Check if repeating this candidate forms both str1 and str2
                if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                    return candidate
        
        return ""

