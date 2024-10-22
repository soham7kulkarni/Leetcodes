# Approach - Count the number of connected components inside grid.
# TC - O(N*N)
# SC - O(N)


class Solution:
    # Main function to find the number of provinces
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  # Number of cities
        visited = [False] * n  # To track visited cities
        province_count = 0  # Count of provinces
        
        # Iterate through each city
        for i in range(n):
            if not visited[i]:  # If city i is unvisited, we start DFS
                self.dfs(i, isConnected, visited)  # Call helper DFS function
                province_count += 1  # Increment province count after DFS finishes
        
        return province_count  # Return the total number of provinces
    
    # DFS helper function to visit all connected cities
    def dfs(self, i, isConnected, visited):
        visited[i] = True  # Mark the current city as visited
        for j in range(len(isConnected)):  # Explore all cities
            if isConnected[i][j] == 1 and not visited[j]:  # If city j is connected and unvisited
                self.dfs(j, isConnected, visited)  # Recursively call DFS for the connected city

        