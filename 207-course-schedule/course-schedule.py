from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            dependent, indepe = edge
            indegree[dependent] += 1
            mapp[indepe].append(dependent)

        q = deque()
        count = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                count += 1

        if not q:
            return False

        while q:
            course = q.popleft()
            children = mapp[course]
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    count += 1

        return count == numCourses
