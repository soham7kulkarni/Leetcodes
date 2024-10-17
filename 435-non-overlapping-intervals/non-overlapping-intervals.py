# TC - O(nlogn)
# SC - O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort intervals by their end times (second element)
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize variables
        # Keep track of the end of the last added non-overlapping interval
        prev_end = intervals[0][1]
        removals = 0  # To count how many intervals need to be removed

        # Step 3: Iterate through intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the current interval's start is less than the previous end, it overlaps
            if intervals[i][0] < prev_end:
                removals += 1  # We need to remove this interval
            else:
                # Otherwise, update the previous end to this interval's end
                prev_end = intervals[i][1]

        return removals
