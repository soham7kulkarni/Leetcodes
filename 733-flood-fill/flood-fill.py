# TC - O(MN)
# SC - O(MN)
# Approach - DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        
        if color == original: return image
        dirs = [[0,1], [0,-1], [-1, 0], [1, 0]]
        self.dfs(image, dirs, original, color, m, n, sr, sc)
        return image

    def dfs(self, image, dirs, original, color, m, n, sr, sc):

        # base
        if sr < 0 or sr == m or sc < 0 or sc == n or image[sr][sc] != original: return
        # logic
        image[sr][sc] = color
        for direction in dirs:
            nr = sr + direction[0]
            nc = sc + direction[1]
            self.dfs(image, dirs, original, color, m, n, nr, nc)