class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height)-1
        area = 0
        while left < right:
            l = right - left
            h = min(height[left], height[right])
            water = l*h
            area = max(area, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area