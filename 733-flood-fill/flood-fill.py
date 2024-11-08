class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dirs = [[0,1], [0,-1], [-1, 0], [1, 0]]
        curr = image[sr][sc]
        if curr == color:
            return image
        self.dfs(image, sr, sc, m, n, dirs, color, curr)
        return image
    def dfs(self, image, sr, sc, m, n, dirs, color, curr):
        # base
        if sr < 0 or sr >= m or sc < 0 or sc >= n or image[sr][sc] != curr: return  
        # logic
        image[sr][sc] = color
        for dir in dirs:
            nr = sr + dir[0]
            nc = sc + dir[1]
            self.dfs(image, nr, nc, m, n, dirs, color, curr)


        