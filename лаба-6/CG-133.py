from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        queue = deque([node])
        old_to_new[node] = Node(node.val)
        
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]

def create_graph(adjList):
    """Создаёт граф из списка смежности (индексы с 1)"""
    if not adjList:
        return None
    
    nodes = {}
    for i in range(1, len(adjList) + 1):
        nodes[i] = Node(i)
    
    for i, neighbors in enumerate(adjList, 1):
        for neighbor_val in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_val])
    
    return nodes[1] if nodes else None

def graph_to_adjList(node):
    if not node:
        return []
    
    adjList = {}
    visited = set()
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        adjList[curr.val] = [n.val for n in curr.neighbors]
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
    
    result = []
    for i in range(1, max(adjList.keys()) + 1):
        result.append(sorted(adjList.get(i, [])))
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Пример 1
    adjList1 = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = create_graph(adjList1)
    clone1 = sol.cloneGraph(graph1)
    print(graph_to_adjList(clone1))
    
    adjList2 = [[]]
    graph2 = create_graph(adjList2)
    clone2 = sol.cloneGraph(graph2)
    print(graph_to_adjList(clone2))

    adjList3 = []
    graph3 = create_graph(adjList3)
    clone3 = sol.cloneGraph(graph3)
    print(graph_to_adjList(clone3))