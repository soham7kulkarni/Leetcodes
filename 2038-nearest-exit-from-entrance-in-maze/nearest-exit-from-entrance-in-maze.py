class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        queue = deque([entrance])
        steps = 0
        visited = set([tuple(entrance)])

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # Check if it's an exit (on the border and not the entrance)
                if (x != entrance[0] or y != entrance[1]) and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1):
                    return steps
                
                # Explore neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            
            steps += 1
        
        return -1
