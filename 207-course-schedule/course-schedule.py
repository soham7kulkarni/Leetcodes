# Approach: BFS with Indegree to maintain no. of prereqs and hashmap for list of dependents
# We don't  maintain size because we are focusing on completion of courses and not on no. of semesters
# TC - O(V+E)
# SC - O(V+E)

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)
        indegree = [0] * numCourses # Indegree to maintain no. of prereqs


        for edge in prerequisites:
            dependent, indepe = edge
            indegree[dependent] += 1 #Update indegree array
            mapp[indepe].append(dependent) #Append dependent to the list

        q = deque()
        count = 0 # To check if we have processed all courses or not

        for i in range(numCourses):
            if indegree[i] == 0: # start with independent node
                q.append(i)
                count += 1

        if not q:
            return False #it means cycle is present, return false

        while q:
            course = q.popleft()
            children = mapp[course] #Go through the children of this node (BFS)
            for child in children:
                indegree[child] -= 1 # Reduce dependency count by 1
                if indegree[child] == 0:
                    q.append(child) # Append any independent node to queue
                    count += 1

        return count == numCourses
