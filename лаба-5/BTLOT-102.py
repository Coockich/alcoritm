from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
        
        return result

def create_tree_from_list(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = create_tree_from_list(arr, 2*i + 1)
    root.right = create_tree_from_list(arr, 2*i + 2)
    return root

sol = Solution()

root = create_tree_from_list([3,9,20,None,None,15,7])
print(sol.levelOrder(root))

root = create_tree_from_list([1])
print(sol.levelOrder(root))

root = create_tree_from_list([])
print(sol.levelOrder(root))

root = create_tree_from_list([1,2,3,4,5,6,7])
print(sol.levelOrder(root))