from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        return validate(root, float('-inf'), float('inf'))

def create_tree_from_list(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = create_tree_from_list(arr, 2*i + 1)
    root.right = create_tree_from_list(arr, 2*i + 2)
    return root

sol = Solution()

root = create_tree_from_list([2, 1, 3])
print(sol.isValidBST(root))

root = create_tree_from_list([5, 1, 4, None, None, 3, 6])
print(sol.isValidBST(root))