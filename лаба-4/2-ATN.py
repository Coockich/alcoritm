class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry:
            return None
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        node = ListNode(s % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            s // 10
        )
        return node

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def from_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

sol = Solution()

l1 = from_list([2, 4, 3])
l2 = from_list([5, 6, 4])
result = sol.addTwoNumbers(l1, l2)
print(to_list(result))

l1 = from_list([0])
l2 = from_list([0])
result = sol.addTwoNumbers(l1, l2)
print(to_list(result))

l1 = from_list([9, 9, 9, 9, 9, 9, 9])
l2 = from_list([9, 9, 9, 9])
result = sol.addTwoNumbers(l1, l2)
print(to_list(result))
