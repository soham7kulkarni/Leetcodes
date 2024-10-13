# TC - O(M*N)
# SC - O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n -1
        result = []
        while top <= bottom and left <= right:
            # top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # bottom row
            # top is changing hence check if bottom exists or not
            # effectively handles inner loop
            # doesn't go over already processed elements
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
            bottom -= 1
            
            # left column
            # right is changing hence check if right exists or not
            # effectively handles inner loop
            # doesn't go over already processed elements
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
            left += 1
        return result
        