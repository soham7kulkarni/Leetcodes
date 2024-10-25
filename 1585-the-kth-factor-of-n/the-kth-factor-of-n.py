# Approach 1 - Traverse from 1 to n. Check if i % n == 0. If yes, add i to factors
# return kth factor

# TC - O(N)
# SC - O(1)

# Approach 2 - Traverse from 1 to sqrt(n). Add i if it is a factor
# Increment k as well and return i if it is kth factor.
# If we dont return i till this part then traverse backwards on all found factors. 
# Add their pairing factor to factors list and return kth factor
# if n is perfect square, we wont add pairing factor to factors since it is already present

# TC - O(sqrt(n))
# SC - O(k)


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # List to store the first half of factors
        factors = []
        
        # Step 1: Find all factors up to sqrt(n)
        for i in range(1, int(n ** 0.5) + 1):
            # If i is a factor of n
            if n % i == 0:
                # Append i to factors
                factors.append(i)
                # Check if this is the k-th factor
                if len(factors) == k:
                    return i
        
        # Step 2: Consider factors greater than sqrt(n)
        # Total number of factors found so far
        total_factors = len(factors)
        
        # Check the larger paired factors in reverse order
        for i in range(total_factors - 1, -1, -1):
            # Calculate the paired factor for factors[i]
            paired_factor = n // factors[i]
            
            # If n is a perfect square, skip the duplicate middle factor
            if paired_factor != factors[i]:
                # Increase the count of total factors
                total_factors += 1
                # If this is the k-th factor, return it
                if total_factors == k:
                    return paired_factor
        
        # If fewer than k factors, return -1
        return -1
        