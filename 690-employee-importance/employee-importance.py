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
        employeeMap = {}
        result = 0
        for employee in employees:
            employeeMap[employee.id] = employee
        queue = deque()
        queue.append(id)
        while queue:
            curr_id = queue.popleft()
            curr_emp = employeeMap[curr_id]
            result += curr_emp.importance
            for sub in curr_emp.subordinates:
                queue.append(sub)
        return result

        