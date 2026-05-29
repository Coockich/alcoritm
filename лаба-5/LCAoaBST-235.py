from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        
        return None

def create_bst_from_list(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = create_bst_from_list(arr, 2*i + 1)
    root.right = create_bst_from_list(arr, 2*i + 2)
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

sol = Solution()

root = create_bst_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
p = find_node(root, 2)
q = find_node(root, 8)
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)

p = find_node(root, 2)
q = find_node(root, 4)
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)

root = create_bst_from_list([2, 1])
p = find_node(root, 2)
q = find_node(root, 1)
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)