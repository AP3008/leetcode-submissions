class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Treat as a graph looking for a course with no prereq's 
        # Perform a DFS until the we find a cycle in the graph because if there is a cycle it becomes impossible to take all fo the courses. 
        # Create an adj. list, and perform dfs on all of those coruses
        # Keep track of the courses seen in a cycle set and a seen set. The seen set is so we can avoid double work. 
        

        adj = { i:[] for i in range(numCourses) }
        for crs, prereq in prerequisites: 
            adj[crs].append(prereq)

        cycle = set()
        seen = set()

        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in seen:
                return True 
            seen.add(crs)
            cycle.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq): return False
            cycle.remove(crs)
            return True 

        for crs in adj:
            if not dfs(crs): return False 
        return True 