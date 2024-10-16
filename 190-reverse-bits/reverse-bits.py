# TC - O(N)
# SC - O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            # Get the last bit of n
            last_bit = n & 1
            
            # Shift result to the left to make space for the last_bit
            result = (result << 1) | last_bit
            
            # Shift n to the right to process the next bit
            n >>= 1
        
        return result
        