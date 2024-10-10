# TC - O(MN)
# SC - O(MN)
# Approach - BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        image[sr][sc] = color
        if color == original: return image
        q = deque()
        q.append(sr)
        q.append(sc)
        dirs = [[0,1], [0,-1], [-1, 0], [1, 0]]
        while q:
            row = q.popleft()
            column = q.popleft()
            if original == color: return image
            for direction in dirs:
                nr = row + direction[0]
                nc = column + direction[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == original:
                    image[nr][nc] = color
                    q.append(nr)
                    q.append(nc)
        return image

        