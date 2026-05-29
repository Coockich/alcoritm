from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        state = [0] * numCourses
        
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            
            state[node] = 2
            return False
        
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True

sol = Solution()

print(sol.canFinish(2, [[1,0]])) 

print(sol.canFinish(2, [[1,0],[0,1]]))
