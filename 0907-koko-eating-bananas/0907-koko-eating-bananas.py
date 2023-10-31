# max value of k will be max(piles). We need to traverse from 1 to max(piles) to check if the given value matches h. We will travers binarily. 
# TC - O(log(max(p))*len(piles))

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        low = 1
        high = n
        res = high
        while(low <= high):
            mid = low + (high-low)//2
            total = 0
            for p in piles:
                total += math.ceil(p/mid)
            if total > h:
                low = mid+1
            else:
                res = min(res,mid)
                high = mid-1
        return res



        