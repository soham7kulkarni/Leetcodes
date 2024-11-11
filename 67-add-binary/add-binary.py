class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Reverse both binary strings to make addition easier from least significant to most
        a = a[::-1]
        b = b[::-1]
        
        # Initialize carry for any overflow from binary addition
        carry = 0
        # Initialize the result as an empty string
        res = ""

        # Loop over the maximum length of the two binary strings
        for i in range(max(len(a), len(b))):
            # Get the digit from string `a` if within bounds, otherwise use 0
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            # Get the digit from string `b` if within bounds, otherwise use 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0
            # Calculate the total by adding both digits and the carry
            total = digitA + digitB + carry
            # Calculate the binary digit to add to result (0 or 1)
            char = str(total % 2)
            # Prepend this character to the result string
            res = char + res
            # Calculate the carry for the next addition (0 or 1)
            carry = total // 2

        # If there's any carry left after the final addition, prepend it to result
        if carry:
            res = str(carry) + res

        # Return the binary result as a string
        return res
