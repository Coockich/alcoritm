from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        first = head
        second = prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

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

head1 = from_list([1,2,3,4])
sol.reorderList(head1)
print(to_list(head1))

head2 = from_list([1,2,3,4,5])
sol.reorderList(head2)
print(to_list(head2))

head3 = from_list([1,2])
sol.reorderList(head3)
print(to_list(head3))

head4 = from_list([1])
sol.reorderList(head4)
print(to_list(head4))