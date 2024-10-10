# Approach 1- Brute Force BFS. From 1 -> 0. Starting from any '1' in the graph.
# Performing BFS on every neighbour. Calculating steps and we return answer.
# TC - O(MN*MN), we perform BFS for 1 node and traverse all other nodes (MN)
# We do so for every other node in the matrix hence MN*MN.

# Approach 2 - Optimal BFS. We go from 0 -> 1. We put all 0's in the queue. While
# determining and putting them in queue, we make all other 1s as -1. We start
# performing BFS but this time we go through all nodes just once hence O(MN)

# TC - O(MN)
# SC - O(MN)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        dirs = [[0,1], [0,-1], [-1, 0], [1, 0]]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    currRow = i
                    currCol = j
                    queue.append(currRow)
                    queue.append(currCol)
                elif mat[i][j] == 1:
                    mat[i][j] = -1
        while queue:
            currRow = queue.popleft()
            currCol = queue.popleft()
            for direction in dirs:
                nr = currRow + direction[0]
                nc = currCol + direction[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[currRow][currCol] + 1
                    queue.append(nr)
                    queue.append(nc)
        return mat

        

        