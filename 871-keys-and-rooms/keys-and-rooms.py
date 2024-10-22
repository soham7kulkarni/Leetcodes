# Approach - run DFS on start node. If we visit node which we haven't visited yet
# We run dfs on that node. When we process node, we add it to visited.
# We should traverse through all nodes to return true 

# TC - O(V+E)
# SC - O(V)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Helper function for DFS traversal
        def dfs(room):
            visited.add(room)  # Mark the room as visited
            for key in rooms[room]:  # Iterate through all keys in the current room
                if key not in visited:  # If the key opens a new room, explore it
                    dfs(key)  # Recursively visit that room

        visited = set()  # Keep track of visited rooms
        dfs(0)  # Start DFS traversal from room 0
        
        # If we visited all rooms, the size of visited set should equal the number of rooms
        return len(visited) == len(rooms)
