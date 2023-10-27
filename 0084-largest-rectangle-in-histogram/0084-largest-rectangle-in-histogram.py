# Approach - when we encounter any column, we need to check if we can extend our previous column. It is possible only when the upcoming column has more height than the previous one. In this case, we just enter index and height of the new column. When we encounter column with less height, we can't extend our previous column/coulmns. At this point, we check first if we have encountered more than one column(It will be present in stack). We calculate the max area at this point simply by considering the height of the first previous column and width. (Mostly it is 1*height). We repeat this till we encounter column with less height. It means all these columns can not be extended hence popping them and updating the maxArea. After this is done, our current column can be extended horizontally till this previous small column hence we update the index for this column as start = index. We append start and height as a pair for this current column.
# Now we need to take care of all columns present in stack. All this can be extended till end hence for every column, we calculate area by taking height of the column and extending it horizontally till the end i.e len(heights)-i. we have updated maxArea at the end to return. 
# TC - O(N),SC- O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))

        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea

        