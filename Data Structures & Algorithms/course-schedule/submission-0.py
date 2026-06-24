class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map the prereq
        req_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            req_map[course].append(prereq)

        visited = set()

        def dfs(course):
            # check for circular
            if course in visited:
                return False
            if req_map[course] == []:
                return True
            
            visited.add(course)
            for prereq in req_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            req_map[course] = []
            return True                
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True