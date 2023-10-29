# solution 1 - linear search : TC - O(mn)
# solution 2 - traverse columns and then row linearly - TC : O(m+n)
# solution 3 - checking range of row and then starting the search: TC - O (m + log n)
# solution 4 - checking ranges of row and columns but with binary search : TC - O(logm + log n)
# solution 5 - putting elements in list and performing binary search : TC - O(log(mn)) - since total no of elements are m*n
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n -1
        while(low<= high):
            mid = low + (high - low)//2
            r = mid//n
            c = mid%n
            if matrix[r][c] == target: return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
            


