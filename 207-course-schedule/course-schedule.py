# Approach: BFS with Indegree to maintain no. of prereqs and
# hashmap for list of dependents
# We don't  maintain size because we are focusing on completion of courses 
# and not on no. of semesters
# TC - O(V+E)
# SC - O(V+E)

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        indegree = [0]*numCourses
        for edge in prerequisites:
            dependent = edge[0]
            independent = edge[1]
            indegree[dependent] += 1
            courseMap[independent].append(dependent)

        queue = deque()
        count = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                count += 1
        
        if not queue:
            return False
        
        while queue:
            course = queue.popleft()
            children = courseMap[course]
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    count += 1
        return count == numCourses