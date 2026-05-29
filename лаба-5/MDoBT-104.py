from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

def create_tree_from_list(arr, i=0):
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