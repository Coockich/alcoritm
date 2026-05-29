from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

def create_tree_from_list(arr, i=0):
    """Создаёт дерево из списка (BFS порядок)"""
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = create_tree_from_list(arr, 2*i + 1)
    root.right = create_tree_from_list(arr, 2*i + 2)
    return root

sol = Solution()

root = create_tree_from_list([3,9,20,None,None,15,7])
print(sol.maxDepth(root))

print(sol.maxDepth(None))

root = TreeNode(1)
print(sol.maxDepth(root))

root = create_tree_from_list([1,2,None,3,None,4,None])
print(sol.maxDepth(root))