# TC - O(N)
# SC - O(N)

# Approach - Built the frequqency map for elements
# If the required difference (k - num) exists with frequency > 0
# We found the element, decrease the frequency by 1 else
# just add element and increase frequency by 1.
# Note - if we found the element pair dont even put the element in map

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_map = {}  # Dictionary to store the frequency of elements
        operations = 0  # Counter for the number of valid pairs

        # Iterate through each number in the array
        for num in nums:
            # Check if the complement (k - num) exists in the map and is available
            complement = k - num
            if count_map.get(complement, 0) > 0:
                # If complement exists, form a pair and reduce the count of complement
                operations += 1
                count_map[complement] -= 1
            else:
                # If complement doesn't exist, increase the count of current number
                count_map[num] = count_map.get(num, 0) + 1

        return operations
        