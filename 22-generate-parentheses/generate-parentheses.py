from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Helper function to perform depth-first search (DFS)
        def dfs(left: int, right: int, s: str):
            # Base case: If the length of the current string is equal to 2n,
            # we have a valid combination of parentheses.
            if len(s) == n * 2:
                res.append(s)  # Add the valid combination to the results
                return 

            # If we can still add an opening parenthesis, do it.
            if left < n:
                dfs(left + 1, right, s + '(')  # Increment left count and add '(' to the string

            # If we can add a closing parenthesis (only if it will not exceed the number of opening ones)
            if right < left:
                dfs(left, right + 1, s + ')')  # Increment right count and add ')' to the string

        res = []  # Initialize the list to hold the result
        dfs(0, 0, '')  # Start the DFS with 0 left and right parentheses used and an empty string
        return res  # Return the list of valid combinations