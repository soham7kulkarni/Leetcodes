
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def __init__(self) -> None:
        self.map = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        deep_copy_curr = self.clone(node)
        queue = deque()
        queue.append(node)
        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in self.map:
                    queue.append(n)
                deep_copy_neighbor = self.clone(n)
                self.map[curr].neighbors.append(deep_copy_neighbor)
        return deep_copy_curr
    def clone(self, node) -> Node:
        if node in self.map:
            return self.map[node]
        newNode = Node(node.val)
        self.map[node] = newNode
        return newNode


        