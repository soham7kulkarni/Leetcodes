from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.map = {} # Map to check if we ahve created the deep copy
        # If no, create one and put in respectively or else just get the deep copy
    
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node: # Base case
            return None
        deepCopyNode = self.clone(node) # Create deep copy in hashmap and get it
        q = deque()
        q.append(node) # Add the starting 1 to q
        while q:
            curr = q.popleft()
            for n in curr.neighbors: # n = 2,4
                if n not in self.map: #If not in map then we need to put in q, create deep copy in hashmap and update the list of neighbours of current
                    q.append(n) #putting in q //2,4
                deepCopy_neighbor = self.clone(n) # Getting the deep copy of 2,4
                self.map[curr].neighbors.append(deepCopy_neighbor) 
                # curr is 1' and we are appending 2',4' as neighbors of 1'
        return deepCopyNode

    def clone(self, node) -> Node:
        if node in self.map:
            return self.map[node] #If deep copy is present, return it
        newNode = Node(node.val) #Else create deep copy of node out of its value
        self.map[node] = newNode # Put this deepcopied node as a value to key of the same node
        return newNode #return deepcopy