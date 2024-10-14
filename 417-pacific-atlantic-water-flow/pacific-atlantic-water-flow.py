# Brute Force - traversing to every cell in grid. For that grid, checking all possibilities of all paths
# Which will lead to both oceans
# TC - O(MN*MN)
# ALso many repeatition while traversing

# Optimal - Starting from ocean. Running DFS on all edge cells.
# addning visited node to respective hashsets as they are visited as well as accessible
# returning if nr, nc goes out of bound or traverse to already visited node
# Checking which cells are accessible thru pacific
# Checking which cells are accessible thru atlantic
# adding these cells to two different hashset
# if cell is appearing in both sets, then adding it to answer

# TC - O(MN)
# SC - O(MN)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()
        dirs = [[0,1], [0,-1], [-1,0], [1, 0]]

        def dfs(r, c, visit, prevHeight, dirs):
            # I want to go only cell with greater heights or else I will return
            if ((r,c) in visit or r < 0 or r == rows or c < 0 or c == cols or heights[r][c] < prevHeight): return
            visit.add((r,c))
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                dfs(nr, nc, visit, heights[r][c], dirs)

        # run dfs on all cells adjacent to pacific 
        for c in range(cols):
            # top row
            dfs(0, c, pac, heights[0][c], dirs)
            # bottom row
            dfs(rows-1, c, atl, heights[rows-1][c], dirs)

        for r in range(rows):
            # left column
            dfs(r, 0, pac, heights[r][0], dirs)
            # right column
            dfs(r, cols-1, atl, heights[r][cols-1], dirs)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        