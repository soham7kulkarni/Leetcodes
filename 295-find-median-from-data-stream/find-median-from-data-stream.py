# TC - O(logn)
# SC - O(n)

# Add a Number: Insert the number into the max-heap 
# if it's less than or equal to the max element; otherwise, insert it into the min-heap.
# Balance the Heaps: Ensure the max-heap has at most one extra element compared to the min-heap 
# by moving elements between the heaps as necessary.
# Find the Median: Return the top of the max-heap if it has one more element, 
# or the average of the tops of both heaps if they are equal in size.

import heapq

class MedianFinder:
    def __init__(self):
        # Step 1: Initialize the two heaps
        self.max_heap = []  # Max-heap (inverted min-heap)
        self.min_heap = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 2: Add a number to the max-heap
        heapq.heappush(self.max_heap, -num)  # Invert num for max-heap
        
        # Step 3: Move the largest element from max-heap to min-heap to balance
        if (self.max_heap and self.min_heap and 
                (-self.max_heap[0] > self.min_heap[0])):
            # Move the largest from max-heap to min-heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Step 4: Balance the sizes of the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move the largest element from max-heap to min-heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            # Move the smallest element from min-heap to max-heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # Step 5: Calculate the median based on the sizes of the heaps
        if len(self.max_heap) > len(self.min_heap):
            # If max-heap has more elements, the median is the top of the max-heap
            return float(-self.max_heap[0])
        else:
            # If both heaps are equal, the median is the average of the tops
            return (-self.max_heap[0] + self.min_heap[0]) / 2
