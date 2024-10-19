# TC - O(N)
# SC - O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize the two smallest variables to infinity
        # 'smallest' will track the smallest number seen so far
        # 'second_smallest' will track the second smallest number seen so far
        smallest = float('inf')
        second_smallest = float('inf')
        
        # Loop through each number in the input array
        for num in nums:
            # If current number is smaller or equal to 'smallest', update 'smallest'
            # This means we are updating the smallest value so far
            if num <= smallest:
                smallest = num
            # If the current number is greater than 'smallest' but smaller or equal to 'second_smallest'
            # update 'second_smallest'. This keeps track of the second smallest number after 'smallest'
            elif num <= second_smallest:
                second_smallest = num
            # If we find a number that is greater than both 'smallest' and 'second_smallest'
            # It means we found a valid increasing triplet, so we return True
            else:
                return True
        
        # If no valid increasing triplet is found, return False
        return False
            