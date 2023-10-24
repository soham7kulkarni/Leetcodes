# Approach - While pushing the temp to stack, comparing it with the top of the stack. If it is greater then popping the top of the stack. Repeating till the stack is empty, since it means it was warmest day. If it islower then just pushing it in stack and waiting for the warmer day. MONOTONIC DECREASING STACK example
# TC - O(N), SC - O(N) 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res
        