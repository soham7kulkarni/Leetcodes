class Solution:
    def climbStairs(self, n: int) -> int:
        # Check if n is zero. If there are no steps, there are zero ways to climb.
        if not n:
            return 0

        # Base case: If there's only 1 step, there's only 1 way to reach it.
        if n == 1:
            return 1

        # Initialize the first two values in the Fibonacci sequence for the staircase problem.
        # 'first' represents the number of ways to reach the previous step.
        # 'second' represents the number of ways to reach the current step.
        first = 1
        second = 1

        # Iterate from step 2 up to n, calculating the number of ways to reach each step.
        for i in range(2, n + 1):
            # Calculate the number of ways to reach the current step.
            current = first + second

            # Move 'second' to 'first' to prepare for the next iteration,
            # as 'first' should represent the previous step in the next round.
            second = first

            # Update 'first' to 'current' as it will now represent the ways to reach the current step.
            first = current

        # After the loop, 'current' holds the number of ways to reach the nth step.
        return current
