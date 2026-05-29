from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                        queue.append((nr, nc))
        
        pacific_queue = deque()
        for c in range(cols):
            pacific_queue.append((0, c))
        for r in range(1, rows):
            pacific_queue.append((r, 0))
        atlantic_queue = deque()
        for c in range(cols):
            atlantic_queue.append((rows - 1, c))
        for r in range(rows - 1):
            atlantic_queue.append((r, cols - 1))
        
        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)
        
        result = list(pacific & atlantic)
        
        return result

sol = Solution()

heights1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(sol.pacificAtlantic(heights1))

heights2 = [[1]]
print(sol.pacificAtlantic(heights2))
