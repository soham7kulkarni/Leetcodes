# TC - we check if partition is substring everytime we generate it
# checking palindrome function takes o(n)
# we apply check to every possible generated combination
# Hence n*2^n

class Solution:
    # Constructor to initialize an instance variable to store results
    def __init__(self):
        # Initialize an empty list to store all palindrome partitions
        self.result = []

    # Main function to return all palindrome partitions of the input string
    def partition(self, s: str) -> List[List[str]]:
        # Start the recursive helper function to generate partitions
        self.helper(s, 0, [])
        # Return the list of all partitions after helper completes
        return self.result

    # Helper function for recursive partition generation
    def helper(self, s: str, idx: int, path: List[str]):
        # Base case: if the current index reaches the end of the string
        if idx == len(s):
            # Add the current partition (path) to the result list
            self.result.append(path[:])
            return
        
        # Recursive case: iterate from the current index to the end of the string
        for i in range(idx, len(s)):
            # Partition the substring from the current index to i (inclusive)
            partition = s[idx:i+1]
            
            # Check if the current substring is a palindrome
            if self.is_palindrome(partition):
                # If it is a palindrome, add the partition to the current path
                path.append(partition)
                
                # Recurse to explore further partitions, starting from the next index
                self.helper(s, i + 1, path)
                
                # Backtrack by removing the last added partition to explore other partitions
                path.pop()

    # Helper function to check if a given string is a palindrome
    def is_palindrome(self, s: str) -> bool:
        # Initialize two pointers: left at the start and right at the end
        left, right = 0, len(s) - 1
        
        # Loop until the pointers meet in the middle
        while left < right:
            # If characters at both pointers don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            # If they match, move both pointers inward
            left += 1
            right -= 1
        
        # If loop completes, all characters matched, so it's a palindrome
        return True
