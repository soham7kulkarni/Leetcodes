# Approach - DFS
# TC - O(M*N)
# SC - O(M*N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dirs = [[0,-1],[-1,0],[0,1],[1,0]]
        orig = image[sr][sc]
        if orig == color: return image
        self.dfs(image, sr, sc, orig, color, dirs)
        return image

    def dfs(self, image, sr, sc, orig, newColor, dirs):
        # base
        if sr < 0 or sr == len(image) or sc < 0 or sc == len(image[0]) or image[sr][sc] != orig: return  # We check if the node is already visited by
        # comapring its original value with current value. If its visited then
        # value will be 2 and not 1

        # logic
        image[sr][sc] = newColor
        for d in dirs:
            nr = sr + d[0]
            nc = sc  + d[1]
            self.dfs(image, nr, nc, orig, newColor, dirs)
