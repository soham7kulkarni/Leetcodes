# Getting 3 hashmaps for rows, columns and squares. Traversing through each element and checking if it is already present in rows, columns and squares. For these hashmaps, keys are row number and column number. Values are all elements belonging to that row or column. For square, we have 9 squares and to identify particular square for that element, we need both row and column. To Uniquely club 9 elements in particular square, we take r//3 and c//3 values in key. With this, we can divide squares in 3 rows and 3 columns with value 0,1,2.
# Time complexity - O(9*9), Space Complexity - O(9*9)
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      rows = defaultdict(set)
      cols = defaultdict(set)
      squares = defaultdict(set)

      for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                return False
            else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c]) #key is (r//3, c//3)
      return True