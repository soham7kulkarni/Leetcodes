# Approach - BFS. Appending seperate row and column value to q
# TC - O(M*N)
# SC - O(M*N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dirs = [[0,-1],[-1,0],[0,1],[1,0]]
        q = deque()
        orig = image[sr][sc]
        image[sr][sc] = color
        q.append(sr)
        q.append(sc)
        while q:
            cr = q.popleft()
            cc = q.popleft()
            if orig == color: return image
            for d in dirs:
                nr = cr + d[0]
                nc = cc + d[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if image[nr][nc] == orig:
                        image[nr][nc] = color
                        q.append(nr)
                        q.append(nc)
        return image

        