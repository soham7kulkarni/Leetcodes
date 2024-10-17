# TC - O(N)
# SC - O(N)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Initialize a result list to store the final intervals
        res = []
        
        # Loop through each interval in the given list
        for i in range(len(intervals)):
            # Case 1: No overlap, and newInterval comes before the current interval
            # If the new interval ends before the current interval starts,
            # we can safely insert newInterval and return the remaining intervals.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]  # Return the merged result immediately
            
            # Case 2: No overlap, and newInterval comes after the current interval
            # If the new interval starts after the current interval ends,
            # we add the current interval to the result as they don't overlap.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlapping intervals
            # If there is overlap, we merge the current interval and the newInterval
            # by taking the minimum start and the maximum end.
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # Earliest start time
                    max(newInterval[1], intervals[i][1])   # Latest end time
                ]
        
        # After looping through all intervals, if newInterval hasn't been added yet,
        # it will be added here to the result list.
        res.append(newInterval)
    
        # Return the result list containing the merged intervals
        return res
