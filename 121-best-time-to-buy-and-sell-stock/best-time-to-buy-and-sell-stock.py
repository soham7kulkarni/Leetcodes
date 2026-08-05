class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        maximum = 0
        for i in range(1, len(prices)):
            smallest = min(smallest, prices[i])
            maximum = max(maximum, prices[i]-smallest)
        return maximum
        