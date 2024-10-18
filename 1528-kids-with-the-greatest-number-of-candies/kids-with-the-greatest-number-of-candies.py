class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
        