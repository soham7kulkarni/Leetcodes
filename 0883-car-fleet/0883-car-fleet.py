# Approach - for a specific car, calculate time of the car to reach destination, which is target-position/speed. If time taken by second car is less than first, then it will surely catch up with first car at one point before reaching destination. Since it does not overtake, it will reduce the speed and will be matched with speed of the first car. hence to consider only first car for further comparisons, we will pop the second car. In this way, we also maintain the number of car fleet.
# TC - o(nlogn), SC - O(N)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
