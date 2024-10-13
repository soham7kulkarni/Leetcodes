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

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for num in nums:
            heapq.heappush(result, num)
            if len(result) > k:
                heapq.heappop(result)
        return result[0]
