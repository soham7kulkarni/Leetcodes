# Approach: BFS with Indegree to maintain no. of prereqs and
# hashmap for list of dependents
# We don't  maintain size because we are focusing on completion of courses 
# and not on no. of semesters
# TC - O(V+E)
# SC - O(V+E)

from collections import defaultdict, deque  # Import defaultdict for easy adjacency list creation and deque for queue operations

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to map each course to the list of dependent courses
        courseMap = defaultdict(list)
        # Initialize indegree array to keep track of the number of prerequisites for each course
        indegree = [0] * numCourses
        
        # Build the graph from prerequisites list
        for edge in prerequisites:
            dependent = edge[0]  # Course that has a prerequisite
            independent = edge[1]  # Course that is the prerequisite
            indegree[dependent] += 1  # Increase the indegree of the dependent course
            courseMap[independent].append(dependent)  # Add dependent course to adjacency list for the prerequisite course

        # Initialize a queue for courses that have no prerequisites
        queue = deque()
        count = 0  # Counter to keep track of how many courses have been processed

        # Enqueue all courses with no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:  # If a course has no prerequisites
                queue.append(i)  # Add it to the queue
                count += 1  # Increase the processed course count

        # If no course with indegree 0, then cycle exists and return False
        if not queue:
            return False

        # Process each course in the queue
        while queue:
            course = queue.popleft()  # Take a course from the queue that has no remaining prerequisites
            children = courseMap[course]  # Get all courses that depend on the current course
            for child in children:  # For each dependent course
                indegree[child] -= 1  # Reduce its indegree by 1
                if indegree[child] == 0:  # If it has no other prerequisites remaining
                    queue.append(child)  # Add it to the queue
                    count += 1  # Increase the processed course count
        
        # Check if we've processed all courses, indicating no cycles
        return count == numCourses  # If count equals numCourses, all courses can be completed; otherwise, a cycle exists
