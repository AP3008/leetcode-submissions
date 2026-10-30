class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = { i:[] for i in range(numCourses) }
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        seen = set()
        cycle = set()
        res = list()

        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in seen:
                return True 
            cycle.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq): return False
            res.append(crs)
            cycle.remove(crs)
            seen.add(crs)
            return True 
        
        for crs in adj:
            if not dfs(crs):
                return []
        return res 
        