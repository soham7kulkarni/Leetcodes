from typing import List

class Solution:
    # Main function to reorder routes
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create adjacency list for the graph
        self.graph = [[] for _ in range(n)]
        
        # Populate the graph
        for u, v in connections:
            self.graph[u].append((v, 1))  # Edge from u to v (1 means it needs to be reversed)
            self.graph[v].append((u, 0))  # Edge from v to u (0 means it does not need to be reversed)

        visited = [False] * n  # Track visited nodes
        return self.dfs(0, visited)  # Start DFS from node 0

    # DFS helper function
    def dfs(self, node: int, visited: List[bool]) -> int:
        visited[node] = True  # Mark the current node as visited
        total_reorders = 0  # Count of reorders needed
        
        # Explore neighbors
        for neighbor, needs_reorder in self.graph[node]:
            if not visited[neighbor]:  # If the neighbor hasn't been visited
                total_reorders += needs_reorder  # Add to count if reordering is needed
                total_reorders += self.dfs(neighbor, visited)  # Continue DFS

        return total_reorders  # Return total reorders needed
