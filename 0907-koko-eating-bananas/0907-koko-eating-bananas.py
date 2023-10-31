class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
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



        