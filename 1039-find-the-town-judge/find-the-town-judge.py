# We maintain the indegrees for all nodes inside the array. 
# If node1 trusts node2, indegree of node1 will decrease by 1 and node2 will increase by 1. 
# This way, we solve both problems, if judge is trusting nobody then he should have indegree n-1.
# Time complexity, O(V+E) since it might happen that v is greater than edges.
# Space complexity O(V)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0]*(n+1)
        for a,b in trust:
            indegrees[a] -= 1 
            indegrees[b] += 1
        for i in range(1, n+1):
            if indegrees[i] == n-1:
                return i
        return -1
        