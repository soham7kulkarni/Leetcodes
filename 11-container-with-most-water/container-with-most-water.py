class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = 0
        h = n-1
        area = 0
        while l < h:

            total = (h-l)*min(height[l],height[h])
            area = max(area, total)
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
        return area

        