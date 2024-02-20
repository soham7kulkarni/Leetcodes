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
        dirs = [[0,-1], [-1,0], [0,1], [1,0]]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append(i)
                    q.append(j)
                if mat[i][j] == 1:
                    mat[i][j] = -1
    
        while q:
            cr = q.popleft()
            cc = q.popleft()
            for d in dirs:
                nr = cr + d[0]
                nc = cc + d[1]
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    q.append(nr)
                    q.append(nc)
                    mat[nr][nc] = mat[cr][cc] + 1  
                    # Just add +1 to previous node
                    # The very first node near 0 will become 1
                    # If previous was 2 then upcoming is 3
                    # Eleminates dist or size variable
                    
        return mat
            

        