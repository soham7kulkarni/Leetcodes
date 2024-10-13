# Approach 1 - sort the array and return element either k or (n-k)
# TC - O(nlogn) SC - O(n)

# Approach 2 - We use min heap. We only store k elements inside heap.
# We add incoming element,
# If it is smaller and if our heap size is greater than k,
# we pop the top element (smallest element)
# In this way, we only maintain k largest elements
# At the end, if k = 2, result[0] is 2nd largest element
# largest element would be result[1] since it is greater than previous and
# to maintain the min_heap it will be placed in 2nd position
# TC - O(nlogk)
# SC - O(k)

# Approach 3 - Using max heap. But now we maintain n-k elements
# These are all small elements but with largest element at the top.
# Whenever we exceed n-k size of heap, we pop that element (it will be largest)
# Compare it with result ele which stores largets element
# Since we maintain n-k, we always deal with kth largest element and not largest
# TC - O(nlog(n-k))
# SC - O(n-k)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_heap = []
        result = float('inf')
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > n-k:
               result = min(result, -heapq.heappop(max_heap)) 
        return result
