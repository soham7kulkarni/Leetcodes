# Approach - 
# To solve the problem, iterate through each building in the binary string, 
# counting the number of valid pairs of opposite types (office and restaurant) 
# before and after the current building. 
# Multiply these counts to find the total number of valid selections

# TC - O(N*N)
# SC - O(1)

class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)  # Get the length of the string
        prefix_ones = [0] * n  # Initialize a prefix sum for '1's
        prefix_zeros = [0] * n  # Initialize a prefix sum for '0's
        
        # Calculate prefix sums
        for i in range(n):
            if i > 0:
                prefix_ones[i] = prefix_ones[i - 1]  # Carry forward the count of '1's
                prefix_zeros[i] = prefix_zeros[i - 1]  # Carry forward the count of '0's
            
            if s[i] == '1':
                prefix_ones[i] += 1  # Increment the count of '1's
            else:
                prefix_zeros[i] += 1  # Increment the count of '0's
        
        total_ways = 0  # Initialize the total ways to 0

        # Iterate through the string again to calculate valid combinations
        for i in range(n):
            if s[i] == '0':  # If the current building is '0'
                # Get count of '1's before i and after i
                ones_before = prefix_ones[i - 1] if i > 0 else 0  # Count of '1's before index i
                ones_after = prefix_ones[-1] - prefix_ones[i]  # Count of '1's after index i
                total_ways += ones_before * ones_after  # Calculate valid combinations
            else:  # If the current building is '1'
                # Get count of '0's before i and after i
                zeros_before = prefix_zeros[i - 1] if i > 0 else 0  # Count of '0's before index i
                zeros_after = prefix_zeros[-1] - prefix_zeros[i]  # Count of '0's after index i
                total_ways += zeros_before * zeros_after  # Calculate valid combinations

        return total_ways  # Return the total number of valid ways
        