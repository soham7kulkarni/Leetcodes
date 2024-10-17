# TC - O(N)
# SC - O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:  # Handle edge case for an empty list
            return 0
        
        max_product = nums[0]  # Initialize max_product with the first element
        min_product = nums[0]  # Initialize min_product with the first element
        result = nums[0]       # Initialize result with the first element
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, swap max_product and min_product
            if num < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(num, max_product * num)  # Calculate maximum product
            min_product = min(num, min_product * num)  # Calculate minimum product
            
            # Update the result with the maximum found so far
            result = max(result, max_product)
        
        return result  # Return the maximum product found
