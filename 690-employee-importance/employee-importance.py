"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# Approach - BFS
# TC - O(V+E)
# SC - O(V)

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = {}
        for e in employees:
            mapp[e.id] = e # Create hashmap with id as key to make search O(1)
        result = 0
        q = deque()
        q.append(id)
        while q:
            eid = q.popleft()
            e = mapp[eid] #As we identified employee in graph, we add
            # importance and determine the subordinates of it. Append them in queue
            result += e.importance
            for subid in e.subordinates:
                q.append(subid)
        return result
                

