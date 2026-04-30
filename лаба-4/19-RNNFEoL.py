from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next

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

head = from_list([1,2,3,4,5])
result = sol.removeNthFromEnd(head, 2)
print(to_list(result))

head = from_list([1])
result = sol.removeNthFromEnd(head, 1)
print(to_list(result))

head = from_list([1,2])
result = sol.removeNthFromEnd(head, 1)
print(to_list(result))

