"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# Approach - DFS
# TC - O(V+E)
# SC - O(V)
class Solution:
    def __init__(self):
        self.result = 0
        self.employeeMap = {}
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for employee in employees:
            self.employeeMap[employee.id] = employee
        self.dfs(id)
        return self.result
    def dfs(self, id) -> None:
        emp = self.employeeMap[id]
        self.result += emp.importance
        for sub in emp.subordinates: 
        #If we are on leaf and there are no subs
        # we automatically come out of the recursion call for that leaf since the processing is completed
        # No need for base case
            self.dfs(sub)
        

        