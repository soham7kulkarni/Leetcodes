# TC - O(N*N)  iterates over each cell of the n x n board once
# SC - O(N*N)  1D array, worst case BFS(n*n) calls
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]*(n*n)
        flag = True
        i = n-1
        j = 0
        idx = 0
        while idx < (n*n):
            if board[i][j] == -1:
                arr[idx] = -1
            else:
                arr[idx] = board[i][j] - 1
            idx += 1
            if flag:
                j += 1
                if j == n:
                    i -= 1
                    j -= 1
                    flag = False
            else:
                j -= 1
                if j < 0:
                    i -= 1
                    j += 1
                    flag = True
        
        q = deque()
        q.append(0)
        arr[0] = -2
        moves = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for l in range(1, 7):
                    newIdx = curr + l
                    if newIdx == n*n - 1:
                        return moves + 1
                    if arr[newIdx] != -2:
                        if arr[newIdx] == -1:
                            q.append(newIdx)
                        else:
                            if arr[newIdx] == n*n-1: return moves+1
                            q.append(arr[newIdx])
                        arr[newIdx] = -2
            moves += 1
        return -1