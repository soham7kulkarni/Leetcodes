# Approach 1 - Building new string and do string manipulations
# Expensive since we will interact with strings frequently

# Approach 2 - putting all char in stack
# So when we encounter *, we just pop top element from stack

# TC - O(N)
# SC - O(N)

class Solution:
    def removeStars(self, s: str) -> str:
        # Step 1: Initialize an empty list to use as a stack
        stack = []
        
        # Step 2: Iterate through each character in the string
        for char in s:
            if char == '*':
                # Step 3: Remove the last character if the current character is a '*'
                if stack:  # Check if the stack is not empty
                    stack.pop()  # Remove the last character
            else:
                # Step 4: Append the current character to the stack
                stack.append(char)
        
        # Step 5: Join the characters in the stack to form the final result
        return ''.join(stack)
        