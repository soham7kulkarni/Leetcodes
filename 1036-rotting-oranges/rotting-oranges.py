# Approach - BFS
# TC - O(M*N)
# SC - O(M*N)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m = len(grid) #number of rows
        n = len(grid[0]) #number of columns
        rotten = 0
        fresh = 0
        time = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten+=1
                    q.append((i,j)) #add all the rotten to the queue before BFS
                elif grid[i][j] == 1:
                    fresh+=1
       
        dirs = [[0,-1], [-1,0], [0,1], [1,0]]
        if not q and fresh == 0: return 0 # We might have just 1 fresh orange hence 0
        while q :
            size = len(q) # for determining time
            for i in range(size):
                curr = q.popleft()
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1: #Check the bounds
                        q.append((nr,nc)) #Append not the value but the co ordinates
                        grid[nr][nc] = 2 #Mark it visited
                        fresh -= 1 
            time += 1   # Increse time by 1 at the end of level processing
        if fresh == 0: return time - 1  #In the end, we process null children of last node and although return to base case i.e queue is empty, we increse time by 1 hence return time - 1
        return -1

        