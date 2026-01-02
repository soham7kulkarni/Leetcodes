# Approach - Calculate the frequency map of all num and then use min heap. Within min-heap, we will put only k elements. As we comapre frequency and push nums within heap, the lowest frequency nums will get replaced and at the end we have only k nums with highest frequency. We return only values within res
# TC - O(nlogk)
# SC - O(n + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

        