from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        second = head

        while second is not None:
            third = second.next
            second.next = first
            first = second
            second = third

        return head
