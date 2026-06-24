class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map the prereq
        req_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            req_map[course].append(prereq)

        res = []
        cycle = set()
        visited = set()

        def dfs(course):
            # check for circular
            if course in cycle:
                return False
            if course in visited:
                return True
            
            # check all prereq for current course
            cycle.add(course)
            for prereq in req_map[course]:
                if not dfs(prereq):
                    return False

            # if prereq are all good, remove it from visited AND
            # since we know that current course is possible, remove its prereq to speed up future visit
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True                
        

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
    